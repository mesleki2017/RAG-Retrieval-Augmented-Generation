- **Embeddings**:
    - These are the main data points, stored as vectors (arrays of numbers). They represent the features or characteristics of the original data in a way that is suitable for similarity searches. #embedding 
- **Metadata**:
    - This is the supplementary data that provides additional context or identifiers for each vector, which can be used to filter results or enrich searches.
- **Indexes**:
    - These structures are created to speed up the retrieval of similar vectors. Depending on the algorithm, the index could be stored in a tree, graph, or other optimized data structure.
- **Persistence**:
    - The vector store typically persists this data in a database or file system, optimized for quick read/write operations. Popular storage formats include JSON, binary files, or database tables.

#Persistence