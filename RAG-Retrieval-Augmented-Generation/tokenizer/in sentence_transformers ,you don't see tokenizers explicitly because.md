```python
from sentence_transformers import SentenceTransformer

# Step 1: Load the pre-trained all-MiniLM-L6-v2 model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 2: Define the input sentence
sentence = "Hugging Face transformers are amazing!"

# Step 3: Generate embeddings for the sentence
embeddings = model.encode(sentence)

# Step 4: Display the results
print(f"Sentence: {sentence}")
print(f"Embedding vector (first 5 dimensions): {embeddings[:5]}...")
print(f"Embedding vector length: {len(embeddings)}")

```

In the last code example, you don't see tokenizers explicitly because the `SentenceTransformer` model (like `all-MiniLM-L6-v2`) abstracts away the tokenization process. #sentence-transformers 

### Here's Why:

1. **Abstracted Tokenization**:
    
    - The `SentenceTransformer` library is built to simplify the use of models for generating embeddings, especially for sentences and paragraphs. It internally handles the tokenization step when you call the `encode` method.
    - When you pass a sentence to `model.encode(sentence)`, the model automatically tokenizes the sentence, processes it, and returns the embedding vector.
2. **User-Friendliness**:
    
    - This abstraction makes the process more user-friendly, particularly for those who are primarily interested in getting embeddings without diving into the details of tokenization, padding, or attention masks.

### How It Works Internally:

- **Tokenization**: Internally, `SentenceTransformer` uses a tokenizer that matches the underlying transformer model (e.g., MiniLM in `all-MiniLM-L6-v2`). This tokenizer breaks down the input text into tokens (e.g., words, subwords), converts them into token IDs, and prepares them for input into the model.
- **Embedding Generation**: After tokenization, the transformer model processes these token IDs to generate embeddings. The `encode` method then returns these embeddings directly.

### Summary:

- **Transformer Model**: The model handles tokenization internally, simplifying the workflow.
- **Embedding Model**: The `SentenceTransformer` is often referred to as an embedding model because its main purpose is to generate embeddings from text.

In summary, the `SentenceTransformer` library abstracts tokenization to make it easier for users to focus on the embeddings, while the underlying transformer model still uses tokenization as part of its process.


### Example with Explicit Tokenization (If Needed):

If you want to see the tokenization step explicitly, you can use the `transformers` library, which `SentenceTransformer` is built on. Here's how you might do that:

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Load the tokenizer and model for 'all-MiniLM-L6-v2'
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

# Tokenize the input sentence
sentence = "Hugging Face transformers are amazing!"
inputs = tokenizer(sentence, return_tensors="pt")

# Generate embeddings using the transformer model
with torch.no_grad():
    outputs = model(**inputs)

# Extract embeddings (use the mean of the token embeddings)
embeddings = outputs.last_hidden_state.mean(dim=1)

# Display the embedding vector
print(f"Sentence: {sentence}")
print(f"Embedding vector (first 5 dimensions): {embeddings[0][:5]}...")

```