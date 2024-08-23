import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFDirectoryLoader
# 1. Load the pre-trained embedding model
embedding_model = SentenceTransformer('C://Users//bulent.cesur//Documents//all-MiniLM-L6-v2')

loader = PyPDFDirectoryLoader("data")
documents = loader.load()
# 2. Example documents or text chunks to index


# 3. Generate embeddings for the documents
embeddings = embedding_model.encode(documents, convert_to_tensor=False)

# 4. Create a FAISS index and add the embeddings
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 distance measure
index.add(np.array(embeddings))

# 5. Define a function to retrieve the most relevant document based on the query
def retrieve_documents(query, k=1):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    retrieved_docs = [documents[i] for i in indices[0]]
    return retrieved_docs

# 6. Initialize the Ollama LLM with the llama3 model
llm = Ollama(model='llama3')

# 7. Define a prompt template to pass retrieved documents to the LLM
prompt_template = """
You are an expert in elevator maintenance. Based on the following document, please answer the user's query.

Document: {document}

Query: {query}

Answer:
"""

# 8. Create a function to generate a response using the LLM and the retrieved documents
def generate_response(query):
    retrieved_docs = retrieve_documents(query, k=1)
    if not retrieved_docs:
        return "No relevant document found."
    
    prompt = PromptTemplate(
        input_variables=["document", "query"],
        template=prompt_template
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(document=retrieved_docs[0], query=query)
    
    return response

# 9. Example query
query = "What are the safety protocols for elevator maintenance?"
response = generate_response(query)

print("Query:", query)
print("Response:", response)
