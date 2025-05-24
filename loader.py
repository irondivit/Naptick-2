import os
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

def load_and_prepare_docs():
    # Load CSV datasets
    dfs = [
        pd.read_csv("data/Sleep_Benchmarks_Reference.csv"),
        pd.read_csv("data/Sleep_health_and_lifestyle_dataset.csv"),
        pd.read_csv("data/Wearable_Dataset.csv"),
        pd.read_csv("data/Sleep_Efficiency.csv")
    ]

    combined_docs = []

    for df in dfs:
        for _, row in df.iterrows():
            text = "\n".join(f"{k}: {v}" for k, v in row.items())
            combined_docs.append(Document(page_content=text))

    # Load PDF research papers
    pdf_paths = ["data/Sleep1.pdf", "data/Sleep2.pdf"]
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        pdf_docs = loader.load()
        combined_docs.extend(pdf_docs)

    # Split all content into chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(combined_docs)
    return docs

def build_rag_agent():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    docs = load_and_prepare_docs()
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

    vectorstore = Chroma.from_documents(docs, embedding=embedding, persist_directory="chroma_store")
    retriever = vectorstore.as_retriever()

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, google_api_key=api_key)

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return rag_chain
