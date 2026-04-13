import streamlit as st
import requests
import os


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/chat")


st.set_page_config(page_title="NovaShop Destek", page_icon="🤖")
st.title("🛍️ NovaShop Akıllı Asistan")
st.caption("İade, kargo veya sipariş durumunuz hakkında sorular sorabilirsiniz.")


if "messages" not in st.session_state:
    st.session_state.messages = []
    # Asistandan ilk selamlama mesajı
    st.session_state.messages.append(
        {"role": "assistant", "content": "Merhaba! NovaShop'a hoş geldiniz. Size nasıl yardımcı olabilirim?"})


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Mesajınızı buraya yazın (Örn: TR1001 kargom nerede?)"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):
        with st.spinner("Asistan yanıtlıyor..."):
            try:

                response = requests.post(API_URL, json={"message": prompt})
                if response.status_code == 200:
                    bot_reply = response.json().get("response", "Bir hata oluştu.")
                else:
                    bot_reply = f"Sunucu hatası: {response.status_code}"
            except requests.exceptions.ConnectionError:
                bot_reply = "Hata: FastAPI sunucusuna ulaşılamıyor. Lütfen arka planda çalıştığından emin olun."


            st.markdown(bot_reply)


    st.session_state.messages.append({"role": "assistant", "content": bot_reply})