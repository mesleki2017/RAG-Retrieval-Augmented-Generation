In this article, we’ll set up a Retrieval-Augmented Generation (RAG) system using Llama 3, LangChain, ChromaDB, and Gradio. No need for paid APIs or GPUs — your local CPU or Google Colab will do.

## Why RAG with Llama 3?

RAG enhances language models by combining them with a retrieval mechanism, improving accuracy and contextual relevance. Llama 3 is an excellent choice for this due to its advanced language capabilities.

## Tools used for

- Llama 3: Our language model.
- LangChain: Framework for LLM applications.
- ChromaDB: Database for storing and querying embedded text data.
- Gradio: Interface for interacting with the model.
- Google Colab: Optional, for efficient computing.

## Setting Up Llama 3 on Google Colab

First select GPU as Hardware accelerator on colaba environment , install and run an **xterm** terminal in Colab to execute shell commands:
```python
!pip install colab-xterm  
%load_ext colabxterm  
%xterm
```
In the terminal that opens, run the following commands to install and set up Llama 3 using Ollama. nomic-embed-text is only if you use it for embedding otherwise you can use llama3 also as an embedding model.

curl -fsSL https://ollama.com/install.sh | sh  
ollama serve & ollama pull llama3 & ollama pull nomic-embed-text

## Testing Llama 3 Integration
```python
!pip -qq install langchain langchain-core langchain-community  
  
from langchain_community.llms import Ollama  
  
llm = Ollama(model="llama3")  
  
response = llm.invoke("What is the meaning of life?")  
print(response)
```

# Incorporating Web Data with BeautifulSoup and LangChain

In this section, we enhance our RAG system by incorporating data fetched from a web URL using BeautifulSoup and LangChain. Here’s how we do it:

- **Fetching Data**: We use BeautifulSoup (bs4) to scrape data from a web page. With LangChain’s WebBaseLoader, we efficiently load the data from the provided URL.
- **Text Splitting**: To handle large documents, we split them into smaller chunks using RecursiveCharacterTextSplitter from LangChain.
- **Embeddings and Vector Store**: Using OllamaEmbeddings and Chroma from LangChain, we create embeddings and a vector store for the text chunks, enabling efficient retrieval.
- **Integration with Llama 3**: We define a function to call the Llama 3 model using Ollama’s chat function, passing the question and context.
- **RAG Setup**: The RAGChain is set up with the retriever using the vector store, combining retrieved documents and calling the Llama 3 model for responses.
- **Gradio Interface**: We create a Gradio interface for users to interact with the RAG system, providing a textbox for questions and displaying the important facts retrieved from the provided context. If desired, you can also incorporate a URL input feature into the Gradio app.

```python
import gradio as gr  
import ollama  
from bs4 import BeautifulSoup as bs  
from langchain.text_splitter import RecursiveCharacterTextSplitter  
from langchain_community.document_loaders import WebBaseLoader  
from langchain_community.vectorstores import Chroma  
from langchain_community.embeddings import OllamaEmbeddings  
  
# Load the data from the web URL  
url = 'http://your_web_URL.com'  
loader = WebBaseLoader(url)  
docs = loader.load()  
  
# Split the loaded documents into chunks  
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  
splits = text_splitter.split_documents(docs)  
  
# Create Ollama embeddings and vector store  
embeddings = OllamaEmbeddings(model="nomic-embed-text") # or use (model = "llama3")  
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)  
  
# Define the function to call the Ollama Llama3 model  
def ollama_llm(question, context):  
formatted_prompt = f"Question: {question}\n\nContext: {context}"  
response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])  
return response['message']['content']  
  
# Define the RAG setup  
retriever = vectorstore.as_retriever()  
  
def rag_chain(question):  
retrieved_docs = retriever.invoke(question)  
formatted_context = "\n\n".join(doc.page_content for doc in retrieved_docs)  
return ollama_llm(question, formatted_context)  
  
# Define the Gradio interface  
def get_important_facts(question):  
return rag_chain(question)  
  
# Create a Gradio app interface  
iface = gr.Interface(  
fn=get_important_facts,  
inputs=gr.Textbox(lines=2, placeholder="Enter your question here..."),  
outputs="text",  
title="RAG with Llama3",  
description="Ask questions about the proveded context",  
)  
  
# Launch the Gradio app  
iface.launch()
```