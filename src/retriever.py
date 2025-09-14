import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from parse_transcripts import load_all_transcripts

class Retriever:
    def __init__(self, folder="transcripts", model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.chunks = load_all_transcripts(folder)

        # Compute embeddings
        texts = [c["text"] for c in self.chunks]
        self.embeddings = self.model.encode(texts, normalize_embeddings=True)

        # Build FAISS index
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(np.array(self.embeddings))

    def search(self, query, top_k=5):
        q_emb = self.model.encode([query], normalize_embeddings=True)
        scores, idxs = self.index.search(np.array(q_emb), top_k)
        results = []
        for i, score in zip(idxs[0], scores[0]):
            c = self.chunks[i]
            c["score"] = float(score)
            results.append(c)
        return results
