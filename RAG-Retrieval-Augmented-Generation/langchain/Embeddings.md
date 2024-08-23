#langchain 
The Embeddings class is a class designed for interfacing with text embedding models. There are lots of embedding model providers (OpenAI, Cohere, Hugging Face, etc) - this class is designed to provide a standard interface for all of them.

Embeddings create a vector representation of a piece of text. This is useful because it means we can think about text in the vector space, and do things like semantic search where we look for pieces of text that are most similar in the vector space.

The base Embeddings class in LangChain provides two methods: one for embedding documents and one for embedding a query. The former takes as input multiple texts, while the latter takes a single text. The reason for having these as two separate methods is that some embedding providers have different embedding methods for documents (to be searched over) vs queries (the search query itself).

https://python.langchain.com/v0.1/docs/integrations/text_embedding/ollama/

# Ollama

Let's load the #Ollama Embeddings class.

```
from langchain_community.embeddings import OllamaEmbeddings
```

#### API Reference:

- [OllamaEmbeddings](https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.ollama.OllamaEmbeddings.html)

```
embeddings = OllamaEmbeddings()
```

```
text = "This is a test document."
```

To generate embeddings, you can either query an invidivual text, or you can query a list of texts.

```
query_result = embeddings.embed_query(text)query_result[:5]
```

```
[-0.09996652603149414, 0.015568195842206478, 0.17670190334320068, 0.16521021723747253, 0.21193109452724457]
```

```
doc_result = embeddings.embed_documents([text])doc_result[0][:5]
```

```
[-0.04242777079343796, 0.016536075621843338, 0.10052520781755447, 0.18272875249385834, 0.2079043835401535]
```

Let's load the Ollama Embeddings class with smaller model (e.g. llama:7b). Note: See other supported models [https://ollama.ai/library](https://ollama.ai/library)

```
embeddings = OllamaEmbeddings(model="llama2:7b")
```

```
text = "This is a test document."
```

```
query_result = embeddings.embed_query(text)
```

```
query_result[:5]
```

```
[-0.09996627271175385, 0.015567859634757042, 0.17670205235481262, 0.16521376371383667, 0.21193283796310425]
```

```
doc_result = embeddings.embed_documents([text])
```

```
doc_result[0][:5]
```

```
[-0.042427532374858856, 0.01653730869293213, 0.10052604228258133, 0.18272635340690613, 0.20790338516235352]
```

[

## llama3.1

Llama 3.1 is a new state-of-the-art model from Meta available in 8B, 70B and 405B parameter sizes.

Tools8B70B

](https://ollama.com/library/llama3.1)