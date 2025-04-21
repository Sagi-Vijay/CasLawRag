import streamlit as st
from rag_pipeline import load_documents, generate_embeddings, retrieve_context, ask_question

st.set_page_config(page_title="CaseLawRAG - Legal AI Assistant")

st.title("⚖️ CaseLawRAG")
st.subheader("Ask questions about your uploaded legal document")

uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file is not None:
    with open("data/input.txt", "w", encoding="utf-8") as f:
        f.write(uploaded_file.read().decode())

    st.success("Document uploaded and saved.")

    # Process embeddings
    generate_embeddings("data/input.txt")

    query = st.text_input("Ask a question about the legal document:")

    if query:
        context = retrieve_context(query)
        answer = ask_question(query, context)
        st.markdown("### 🧠 Answer:")
        st.write(answer)
