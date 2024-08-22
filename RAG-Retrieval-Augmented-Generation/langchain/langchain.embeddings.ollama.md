#langchain
https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.ollama.OllamaEmbeddings.html
```python

from langchain_community.embeddings import OllamaEmbeddings
ollama_emb = OllamaEmbeddings(
    model="llama:7b",
)
r1 = ollama_emb.embed_documents(
    [
        "Alpha is the first letter of Greek alphabet",
        "Beta is the second letter of Greek alphabet",
    ]
)
r2 = ollama_emb.embed_query(
    "What is the second letter of Greek alphabet"
)

```