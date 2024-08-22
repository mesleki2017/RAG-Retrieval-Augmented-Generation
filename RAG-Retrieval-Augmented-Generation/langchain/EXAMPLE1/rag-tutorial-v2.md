#langchain
https://github.com/pixegami/rag-tutorial-v2


```python
from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
```


https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.ollama.OllamaEmbeddings.html

**"nomic-embed-text"** in the context of `OllamaEmbeddings(model="nomic-embed-text")` refers to a specific pre-trained model from Ollama, designed for embedding text data.

**Ollama** is a platform that provides access to various language models and tools. One of these tools is the `OllamaEmbeddings` class, which allows you to generate embeddings for text using different pre-trained models.

**"nomic-embed-text"** is the name of the particular model you're selecting. This model is likely trained on a large amount of text data and has been optimized for generating high-quality embeddings.

**In summary:**

- **OllamaEmbeddings:** A class for generating embeddings.
- **"nomic-embed-text"**: A specific pre-trained model from Ollama.

By using `OllamaEmbeddings(model="nomic-embed-text")`, you're instructing the Ollama platform to use the "nomic-embed-text" model to generate embeddings for your input text.




