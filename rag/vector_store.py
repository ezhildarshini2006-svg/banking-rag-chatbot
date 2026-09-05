from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from rag.embeddings import get_embeddings

def create_vector_store(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    documents = [Document(page_content=chunk) for chunk in chunks]
    return FAISS.from_documents(documents, get_embeddings())
