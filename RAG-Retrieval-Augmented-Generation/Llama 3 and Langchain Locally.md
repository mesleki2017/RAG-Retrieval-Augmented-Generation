```python
#https://drlee.io/run-llama-3-and-langchain-locally-in-google-colab-to-build-a-rag-solution-a-step-by-step-guide-1077eb630e6b

from langchain_community.llms import Ollama

from langchain.chains import RetrievalQA

from langchain.vectorstores import Chroma

from sentence_transformers import SentenceTransformer

from langchain.embeddings import SentenceTransformerEmbeddings

from langchain.text_splitter import CharacterTextSplitter

from langchain.docstore.document import Document

  

# Initialize the Llama 3 model

llm = Ollama(model="llama3")

  

# Create an embedding model

embeddings = SentenceTransformerEmbeddings(model_name='C://Users//bulent.cesur//Documents//all-MiniLM-L6-v2')

  

# Prepare documents

documents = [

    Document(page_content="The capital of Florida is Tallahassee.", metadata={"id": 0}),

    Document(page_content="Florida is known for its beautiful beaches and warm climate.", metadata={"id": 1}),

    Document(page_content="The largest city in Florida by population is Jacksonville.", metadata={"id": 2}),

    Document(page_content="The President of Miami Dade College is President Madeline Pumariega.", metadata={"id": 3}),

    Document(page_content="The Provost of Miami Dade College is Dr. Malou C. Harrison.", metadata={"id": 4}),

    Document(page_content="Dr. Ernesto Lee is an AI and Data Analytics Professor on the Kendall Campus at Miami Dade College.", metadata={"id": 5})

]

  

# Create Chroma vector store

vector_store = Chroma.from_documents(documents, embedding=embeddings)

  

# Load the QA chain

qa_chain = RetrievalQA.from_chain_type(

    llm=llm,

    chain_type="stuff",

    retriever=vector_store.as_retriever()

)

  

# Use the QA chain to retrieve relevant documents and generate a response

queries = [

    "What is the capital of Florida?",

    "Who is the President of Miami Dade College?",

    "Who is the Provost of Miami Dade College?",

    "Who is Dr. Ernesto Lee?"

]

  

for query in queries:

    response = qa_chain.run(query)

    print(f"Query: {query}\nResponse: {response}\n")
```

[link](https://drlee.io/run-llama-3-and-langchain-locally-in-google-colab-to-build-a-rag-solution-a-step-by-step-guide-1077eb630e6b)