📄 Docling + OpenAI + FAISS Pipeline

This project demonstrates an end-to-end RAG-ready pipeline using:

Docling
 for PDF/document conversion

HybridChunker for structure-aware text chunking

OpenAI embeddings
 for vectorization

FAISS
 for fast similarity search

🚀 Features

Convert PDFs into structured text with Docling

Apply hybrid chunking (structure + token-aware)

Generate embeddings with OpenAI models (text-embedding-3-small / text-embedding-3-large)

Store vectors in a FAISS index

Run semantic search queries over document chunks

🛠️ Installation

Clone the repo

git clone <your-repo-url>
cd <your-repo>


Create environment

conda create -n docling_rag python=3.10 -y
conda activate docling_rag


Install requirements

pip install -r requirements.txt


Set your OpenAI API key

echo "OPENAI_API_KEY=your_api_key_here" > .env

📦 Requirements

requirements.txt includes:

torch>=2.1
transformers>=4.46.2
accelerate>=0.30.0
tqdm==4.66.1
python-dotenv==1.0.0
requests==2.31.0

docling
docling-core
docling-ibm-models

langchain==0.3.27
langchain-docling==1.1.0
langchain_huggingface==0.3.1
faiss-cpu==1.8.0
openai>=1.0.0

⚡ Usage
1. Run the pipeline
python rag_pipeline.py

2. What it does

Loads https://arxiv.org/pdf/2408.09869

Converts it into a DoclingDocument

Splits it into chunks (~512 tokens each)

Embeds chunks with OpenAI embeddings

Stores embeddings in a FAISS index

Runs a demo query (e.g., “What problem does Docling aim to solve?”) against the index

3. Example output
✅ Total chunks: 27
✅ ✅ FAISS index built with 27 vectors

🔎 Top 3 results:
1. Neural networks are widely used in...
2. Training requires a large dataset...
3. The model achieved strong accuracy...

EXAMPLE QUESTIONS 
How is Docling different from traditional PDF parsers like pdfplumber or PyMuPDF?
What are the main components of Docling’s architecture?
How does Docling integrate with Hugging Face and LangChain?
On which datasets was Docling evaluated?
What are the limitations of Docling, and what future work is proposed?
How can Docling be used in Retrieval-Augmented Generation (RAG) pipelines?

