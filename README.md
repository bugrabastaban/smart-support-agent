NovaShop Akıllı Destek Asistanı

Selamlar. Bu projeyi, standart chatbotlardan ziyade, arka planda gerçekten bir iş akışı yürüten bir yapay zeka sistemi kurmak için geliştirdim.
Temelde bir e-ticaret sitesi (hayali NovaShop) için müşteri hizmetleri asistanı. Asistan sadece genel geçer laflar üretmiyor; eğer kullanıcı iade veya kargo kurallarını sorarsa gidip şirketin PDF'lerini okuyor (RAG), eğer "kargom nerede" diye spesifik bir sipariş sorarsa gidip veritabanına sorgu atıyor (Tool Calling).

Neler Kullandım?

Model & Orkestrasyon: Gemini 2.5 Flash ve LangChain (Ajanın karar verme ve tool kullanma mekanizması için)

RAG & Vektör DB: ChromaDB ve HuggingFace Embeddings (Politika dokümanlarını parçalayıp anlamlandırmak için)

Backend: FastAPI (Sistemin asenkron ve API tabanlı çalışması için)

Frontend: Streamlit (Chat arayüzü için)

Altyapı: Docker & Docker Compose
