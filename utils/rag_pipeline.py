import os
from dotenv import load_dotenv
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from transformers import AutoTokenizer
from openai import OpenAI
import faiss
import numpy as np

# ---------------------------------------------------
# 1. Setup
# ---------------------------------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

pdf_path = "example.pdf"  # change to your PDF path

# ---------------------------------------------------
# 2. Convert PDF → DoclingDocument
# ---------------------------------------------------
converter = DocumentConverter()

result = converter.convert("https://arxiv.org/pdf/2408.09869")
doc = result.document

# ---------------------------------------------------
# 3. Chunking with HybridChunker
# ---------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
chunker = HybridChunker(tokenizer=tokenizer, max_tokens=512, merge_peers=True)

chunks = list(chunker.chunk(dl_doc=doc))
print(f"✅ Total chunks: {len(chunks)}")

# ---------------------------------------------------
# 4. OpenAI embeddings
# ---------------------------------------------------
def embed_text(text):
    resp = client.embeddings.create(
        model="text-embedding-3-small",  # or text-embedding-3-large
        input=text
    )
    return np.array(resp.data[0].embedding, dtype="float32")

embeddings = [embed_text(c.text) for c in chunks]
dim = len(embeddings[0])

# ---------------------------------------------------
# 5. FAISS index
# ---------------------------------------------------
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

print(f"✅ FAISS index built with {index.ntotal} vectors")

# ---------------------------------------------------
# 6. Example search
# ---------------------------------------------------
query = "What problem does Docling aim to solve?"
query_emb = embed_text(query)

D, I = index.search(np.array([query_emb]), k=3)

print("\n🔎 Top 3 results:")
for rank, idx in enumerate(I[0]):
    print(f"{rank+1}. {chunks[idx].text[:200]}...\n")
