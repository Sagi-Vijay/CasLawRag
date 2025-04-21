from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

os.environ["OPENAI_API_KEY"] = "sk-..."  # Replace with your key

def load_documents(file_path="data/input.txt"):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents

def generate_embeddings(file_path="data/input.txt"):
    documents = load_documents(file_path)
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)
    db.save_local("embeddings")

def retrieve_context(query):
    db = FAISS.load_local("embeddings", OpenAIEmbeddings())
    retriever = db.as_retriever()
    docs = retriever.get_relevant_documents(query)
    return docs

def ask_question(query, docs):
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=None)
    return llm.predict(context=docs, question=query)
