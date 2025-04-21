# 🧠 CaseLawRAG - Smart Legal Case Assistant

**CaseLawRAG** is an AI-powered legal assistant that combines Retrieval-Augmented Generation (RAG) with Large Language Models (LLMs) like GPT to answer legal queries with citations. It’s built for fast and accurate insights from large legal document repositories.

This project is a GenAI-powered Retrieval-Augmented Generation (RAG) application designed to help users search and summarize case law documents using Large Language Models (LLMs).

### 🔍 Features
- Upload legal documents (PDF)
- Ask questions and get accurate answers based on the documents
- Built using LangChain, OpenAI, FAISS, and Streamlit

### 💻 Technologies Used
- Python
- Streamlit
- LangChain
- FAISS Vector Store
- OpenAI GPT-4 API
- RAG (Retrieval-Augmented Generation)

---

## 🧩 Features

- 📂 Upload & process legal case files
- 🔎 Embedding-based semantic search  
- 🧠 GPT answers based on real documents  
- ✅ Citations shown to reduce hallucinations  
- ⚡ Simple UI with fast responses

---

## 🚀 Getting Started (Local)

bash
CaseLawRAG/
│
├── data/               # Legal documents go here
├── embeddings/         # FAISS vector DB saved here
├── app.py              # Streamlit frontend
├── rag_pipeline.py     # Backend logic (Load, Embed, Retrieve, Answer)
├── requirements.txt    # Python packages
└── README.md

git clone https://github.com/Sagi-Vijay/CaseLawRAG.git
cd CaseLawRAG
pip install -r requirements.txt
streamlit run app.py

