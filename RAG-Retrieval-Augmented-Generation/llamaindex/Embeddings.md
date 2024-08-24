#embedding 
Embeddings are used in #LlamaIndex to represent your documents using a sophisticated numerical representation. Embedding models take text as input, and return a long list of numbers used to capture the #semantic s of the text. These embedding models have been trained to represent text this way, and help enable many applications, including search!

At a high level, if a user asks a question about dogs, then the embedding for that question will be highly similar to text that talks about dogs.

When calculating the similarity between embeddings, there are many methods to use (dot product, cosine similarity, etc.). By default, LlamaIndex uses cosine similarity when comparing embeddings.

There are many embedding models to pick from. By default, LlamaIndex uses `text-embedding-ada-002` from OpenAI. We also support any embedding model offered by Langchain [here](https://python.langchain.com/docs/modules/data_connection/text_embedding/), as well as providing an easy to extend base class for implementing your own embeddings.


