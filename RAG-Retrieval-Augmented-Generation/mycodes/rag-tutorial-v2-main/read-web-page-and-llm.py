
#https://github.com/Shubhamsaboo/awesome-llm-apps/blob/aaf5b72fe997b41e67f7d2a990e3e49bdaa65101/llama3.1_local_rag/llama3.1_local_rag.py
import ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings


# Get the webpage URL from the user
webpage_url = "https://www.elektriktesisatportali.com/elektrik-tesisatlarinda-kisa-devre-akimlarinin-hesaplanmasi.html"
#https://www.elektriktesisatportali.com/elektrik-tesisatlarinda-kisa-devre-akimlarinin-hesaplanmasi.html
if webpage_url:
    # 1. Load the data
    loader = WebBaseLoader(webpage_url ,verify_ssl=False)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    splits = text_splitter.split_documents(docs)

    # 2. Create Ollama embeddings and vector store
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    # 3. Call Ollama Llama3 model
    def ollama_llm(question, context):
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']

    # 4. RAG Setup
    retriever = vectorstore.as_retriever()

    def combine_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_chain(question):
        retrieved_docs = retriever.invoke(question)
        formatted_context = combine_docs(retrieved_docs)
        return ollama_llm(question, formatted_context)

    print("web page loaded")

    # Ask a question about the webpage
    prompt = "Trafonun sekonder tarafındaki kısa devre akımı nedir"

    # Chat with the webpage
    if prompt:
        result = rag_chain(prompt)
        print(result)