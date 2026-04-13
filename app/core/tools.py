from langchain.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.db.mock_data import mock_orders
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)


@tool
def search_policies(query: str) -> str:
    """
    Kullanıcının iade, kargo ücreti, gizlilik veya genel şirket kurallarıyla ilgili
    sorularını yanıtlamak için politika dokümanlarında (RAG) arama yapar.
    """
    print(f"--> [SİSTEM] RAG Aracı Çalıştı. Sorgu: {query}")
    docs = db.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in docs])


@tool
def check_order(order_id: str) -> str:
    """
    Kullanıcının sipariş durumunu, kargo sürecini veya teslimat tarihini
    kontrol etmek için kullanılır. Girdi olarak sipariş numarası (Örn: TR1001) alır.
    """
    print(f"--> [SİSTEM] Veritabanı Aracı Çalıştı. Sipariş No: {order_id}")
    order = mock_orders.get(order_id.upper())

    if order:
        return f"Sipariş Durumu: {order['status']}, Tahmini Teslimat: {order['expected_delivery']}, İçerik: {', '.join(order['items'])}"

    return "Bu sipariş numarasına ait bir kayıt bulunamadı. Lütfen numarayı kontrol edin."