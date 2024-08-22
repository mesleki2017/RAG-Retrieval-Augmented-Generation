#langchain
1. **Load**: First we need to load our data. This is done with [Document Loaders](https://python.langchain.com/v0.2/docs/concepts/#document-loaders).
2. **Split**: [Text splitters](https://python.langchain.com/v0.2/docs/concepts/#text-splitters) break large `Documents` into smaller #chunks. This is useful both for indexing data and for passing it in to a model, since large chunks are harder to search over and won't fit in a model's finite context window.
3. **Store**: We need somewhere to store and index our splits, so that they can later be searched over. This is often done using a [VectorStore](https://python.langchain.com/v0.2/docs/concepts/#vector-stores) and [Embeddings](https://python.langchain.com/v0.2/docs/concepts/#embedding-models) model.

