https://weaviate.io/blog/how-to-choose-an-embedding-model
https://huggingface.co/spaces/mteb/leaderboard

[Vector embeddings](https://weaviate.io/blog/vector-embeddings-explained) power modern search and Retrieval-Augmented Generation (RAG) applications. Embeddings capture the semantic meaning of data objects (e.g., text) and represent them in an array of numbers. In today’s Generative AI applications, these vector embeddings are typically generated with so-called embedding models.

## Step 1: Identify your use case[​](https://weaviate.io/blog/how-to-choose-an-embedding-model#step-1-identify-your-use-case "Direct link to Step 1: Identify your use case")

Would a general-purpose model be sufficient for what you are trying to achieve, or do you have specific needs, such as modality (e.g., text only or multimodal), subject domain (e.g., coding, law, medical, multilingual, etc.), and deployment mode? In most cases, starting with a general-purpose model for your desired modalities would be a sensible baseline.

## Step 2: Select a baseline model[​](https://weaviate.io/blog/how-to-choose-an-embedding-model#step-2-select-a-baseline-model "Direct link to Step 2: Select a baseline model")

The [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) is a good starting point for getting an overview of the current landscape of the wide range of proprietary and open source text embedding models. For each embedding model, the MTEB lists various metrics, such as the model size, memory usage, embedding dimensions, maximum number of tokens, and its score for tasks such as retrieval, summarization, etc.

Here are a few considerations for choosing the best model for your application:

- **Task:** On the top of the MTEB Leaderboard, you will see various tabs. You first have to decide whether you want an all-rounder or if you can find a task (classification, clustering, retrieval, summarization, etc.) that matches your specific use case. For example, if you are building an RAG application, you might want to look closer at the “Retrieval” task. You might also want to refine your selection if you have more specific needs, such as a specific language (e.g., English, Chinese, French, Polish) or domain (e.g., law).
- **Score**: This will show you how well the model performs on a specific benchmark dataset or across multiple benchmark datasets. Depending on the task, different [evaluation metrics](https://weaviate.io/blog/retrieval-evaluation-metrics) are used. Usually, these metrics can take values between 0 and 1, where higher values indicate a better performance.
- **Model size and memory usage:** These give you an idea of the computational resources required to run the model. While retrieval performance scales with model size, it is important to note that model size also directly impacts latency. Additionally, it is worth mentioning that larger models can also overfit and thus underperform in production. Thus, you want to aim for a good latency-performance trade-off for a production setup. Ideally, start with a small, lightweight model to be able to build a baseline upon which you can iterate quickly. Once your pipeline works, you can switch out the model with a bigger and more performant one later.
- **Embedding dimensions**: This is the length of the embedding vector. While larger embedding dimensions can capture more nuanced details and relationships in the data, they aren't necessarily always better. Do you really need 2048 dimensions to chat with a PDF? Probably not. On the other hand, smaller embedding dimensions offer faster inference and are more storage- and memory-efficient. Thus, you will want to aim for a good trade-off between capturing the complexity of data and operational efficiency.
- **Max tokens**: This is the maximum number of tokens that can be converted into a single embedding. For common RAG applications, a good chunk size for an embedding is typically about a single paragraph of text or less. In this case, models with max tokens of 512 should be sufficient. However, there will be special cases where you need to embed longer source texts that require models with a larger context window.
