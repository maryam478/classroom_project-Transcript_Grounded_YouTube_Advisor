from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from transformers import AutoTokenizer

# 1. Convert PDF → DoclingDocument
converter = DocumentConverter()
result = converter.convert("https://arxiv.org/pdf/2408.09869")
doc = result.document   # DoclingDocument

# 2. Use a HuggingFace tokenizer
# MiniLM is a good fit if you plan embeddings with sentence-transformers
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# 3. Initialize HybridChunker
chunker = HybridChunker(
    tokenizer=tokenizer,
    max_tokens=512,     # matches MiniLM’s max context length
    merge_peers=True,   # merges sibling nodes when short
)

# 4. Chunk the document
chunks = list(chunker.chunk(dl_doc=doc))
print(f"Total chunks: {len(chunks)}")
print(chunks[0].text)   # see first chunk

































# from docling.chunking import HybridChunker
# from docling.document_converter import DocumentConverter
# from dotenv import load_dotenv
# from openai import OpenAI
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from tokenizer import OpenAITokenizerWrapper
# from transformers import AutoTokenizer
# import os

# load_dotenv()

# # Initialize OpenAI client (make sure you have OPENAI_API_KEY in your environment variables)


# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# # tokenizer = OpenAITokenizerWrapper()  # Load our custom tokenizer for OpenAI
# # MAX_TOKENS = 8191  # text-embedding-3-large's maximum context length
# tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")


# # --------------------------------------------------------------
# # Extract the data
# # --------------------------------------------------------------

# converter = DocumentConverter()
# result = converter.convert("https://arxiv.org/pdf/2408.09869")


# # --------------------------------------------------------------
# # Apply hybrid chunking
# # --------------------------------------------------------------

# chunker = HybridChunker(
#     tokenizer=tokenizer,
#     max_tokens=512,
#     merge_peers=True,
# )

# chunk_iter = chunker.chunk(dl_doc=result.document)
# chunks = list(chunk_iter)

# len(chunks)