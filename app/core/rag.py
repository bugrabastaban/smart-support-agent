from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "e_ticaret_politikalar.pdf")
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

def create_vector_db():
    print("Doküman yükleniyor...")

    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Toplam {len(chunks)} parça oluşturuldu.")


    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


    print("Vektörler ChromaDB'ye kaydediliyor...")
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_PATH
    )
    print("Vector DB başarıyla oluşturuldu ve 'chroma_db' klasörüne kaydedildi!")

if __name__ == "__main__":
    create_vector_db()