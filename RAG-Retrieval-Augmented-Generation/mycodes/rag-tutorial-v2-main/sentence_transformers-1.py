from sentence_transformers import SentenceTransformer

model = SentenceTransformer('C://Users//bulent.cesur//Documents//all-MiniLM-L6-v2')



# Step 2: Define the input sentence
sentence = "Hugging Face transformers are amazing!"

# Step 3: Generate embeddings for the sentence
embeddings = model.encode(sentence)

# Step 4: Display the results
print(f"Sentence: {sentence}")
print(f"Embedding vector (first 5 dimensions): {embeddings[:5]}...")
print(f"Embedding vector length: {len(embeddings)}")