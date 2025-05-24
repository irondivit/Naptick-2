import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def build_agent():
    # Load .env variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3,
        google_api_key=api_key
    )
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory, verbose=True)
    return chain
