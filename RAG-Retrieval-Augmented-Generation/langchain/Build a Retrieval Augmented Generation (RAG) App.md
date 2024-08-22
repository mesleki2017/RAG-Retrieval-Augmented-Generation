One of the most powerful applications enabled by LLMs is sophisticated question-answering (Q&A) chatbots. These are applications that can answer questions about specific source information. These applications use a technique known as Retrieval Augmented Generation, or RAG

- https://github.com/pixegami/rag-tutorial-v2
- https://python.langchain.com/v0.2/docs/tutorials/rag/


**Indexing**: a pipeline for ingesting data from a source and indexing it. _This usually happens offline._

**Retrieval and generation**: the actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.