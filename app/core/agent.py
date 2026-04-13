from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents  import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os


from app.core.tools import search_policies, check_order


load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


tools = [search_policies, check_order]


prompt = ChatPromptTemplate.from_messages([
    ("system", """Sen NovaShop e-ticaret platformunun profesyonel ve yardımcı müşteri hizmetleri asistanısın.
    Görevlerin:
    1) İade koşulları, kargo politikası veya gizlilik gibi şirket kuralları sorulduğunda DAİMA 'search_policies' aracını kullan.
    2) Müşteri belirli bir siparişin durumunu (Örn: TR1001) sorduğunda DAİMA 'check_order' aracını kullan.

    Kurallar:
    - Bilgiyi asla uydurma, sadece araçlardan dönen sonuçlara göre cevap ver.
    - Cevapların kısa, net ve müşteri temsilcisi kibarlığında olsun.
    """),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),  # Ajanın düşünme ve araç kullanma adımlarını tutar
])


agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def run_agent(user_message: str) -> str:
    """FastAPI'den çağrılacak ana fonksiyon"""
    try:
        response = agent_executor.invoke({"input": user_message})
        output = response["output"]


        if isinstance(output, list):
            clean_text = ""
            for item in output:
                if isinstance(item, dict) and "text" in item:
                    clean_text += item["text"]
                elif isinstance(item, str):
                    clean_text += item
            return clean_text


        return output

    except Exception as e:
        return f"Üzgünüm, şu an sistemlerimizde bir yoğunluk var. Hata: {str(e)}"

if __name__ == "__main__":
    test_message = "TR1003 numaralı siparişim ne alemde?"
    print("\n--- Test Başlıyor ---")
    print(run_agent(test_message))