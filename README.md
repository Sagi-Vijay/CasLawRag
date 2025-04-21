# 🧠 CaseLawRAG - Smart Legal Case Assistant

**CaseLawRAG** is an AI-powered legal assistant that combines Retrieval-Augmented Generation (RAG) with Large Language Models (LLMs) like GPT to answer legal queries with citations. It’s built for fast and accurate insights from large legal document repositories.

## 💼 Use Case
Upload court case summaries, contracts, or legal text files — ask natural language questions — get reliable, cited answers.

---

## ⚙️ Tech Stack

- **Python**  
- **LangChain + OpenAI (GPT-3.5/4)**  
- **FAISS Vector Search**  
- **Streamlit UI**  
- **RAG Pipeline** (custom-built)

---

## 🧩 Features

- 📂 Upload & process legal case files
-  CaseLawRAG/
│
├── data/               # Legal documents go here
├── embeddings/         # FAISS vector DB saved here
├── app.py              # Streamlit frontend
├── rag_pipeline.py     # Backend logic (Load, Embed, Retrieve, Answer)
├── requirements.txt    # Python packages
└── README.md

- 🔎 Embedding-based semantic search  
- 🧠 GPT answers based on real documents  
- ✅ Citations shown to reduce hallucinations  
- ⚡ Simple UI with fast responses

---

## 🚀 Getting Started (Local)

```bash
git clone https://github.com/YOUR-USERNAME/CaseLawRAG.git
cd CaseLawRAG
pip install -r requirements.txt
streamlit run app.py
