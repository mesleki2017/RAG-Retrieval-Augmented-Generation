```python
import argparse
import os
import shutil
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    """
    Retrieves the embedding function for use with Chroma.

    Returns:
        OllamaEmbeddings: The embedding function.
    """
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

CHROMA_PATH = "chroma"
DATA_PATH = "data"

def main():
    """
    Main function for processing and storing documents in Chroma.

    Args:
        args: Command-line arguments.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()

    # Clear the database if requested
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Load documents from the specified directory
    documents = load_documents()

    # Split documents into chunks
    chunks = split_documents(documents)

    # Add chunks to Chroma
    add_to_chroma(chunks)

def load_documents():
    """
    Loads documents from the specified directory.

    Returns:
        list[Document]: A list of loaded documents.
    """
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

def split_documents(documents: list[Document]):
    """
    Splits documents into chunks.

    Args:
        documents: A list of documents.

    Returns:
        list[Document]: A list of document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def add_to_chroma(chunks: list[Document]):
    """
    Adds document chunks to Chroma.

    Args:
        chunks: A list of document chunks.
    """
    # Load the existing Chroma database
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Calculate chunk IDs
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or update documents in Chroma
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if new_chunks:
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        print("✅ No new documents to add")

def calculate_chunk_ids(chunks):
    """
    Calculates chunk IDs for documents.

    Args:
        chunks: A list of document chunks.

    Returns:
        list[Document]: A list of document chunks with calculated IDs.
    """
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add the chunk ID to the metadata
        chunk.metadata["id"] = chunk_id

    return chunks

def clear_database():
    """
    Clears the Chroma database.
    """
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

if __name__ == "__main__":
    main()
```

**Step-by-Step Explanation:**

1. **Import necessary modules:**
    
    - `argparse`: For parsing command-line arguments.
    - `os`: For interacting with the operating system.
    - `shutil`: For removing directories.
    - `PyPDFDirectoryLoader`: For loading PDF documents from a directory.
    - `RecursiveCharacterTextSplitter`: For splitting text into chunks.
    - `Document`: For representing documents.
    - `Chroma`: For creating a vector store.
    - `OllamaEmbeddings`: For generating embeddings.
2. **Define the `get_embedding_function()` function:**
    
    - Retrieves the embedding function from Ollama.
3. **Define global variables:**
    
    - `CHROMA_PATH`: Path to the Chroma database.
    - `DATA_PATH`: Path to the data directory.
4. **Define the `main()` function:**
    
    - Parses command-line arguments.
    - Clears the Chroma database if the `--reset` flag is provided.
    - Loads documents from the `DATA_PATH` directory.
    - Splits documents into chunks.
    - Adds chunks to the Chroma database.
5. **Define the `load_documents()` function:**
    
    - Loads documents from the specified directory using `PyPDFDirectoryLoader`.
6. **Define the `split_documents()` function:**
    
    - Splits documents into chunks using `RecursiveCharacterTextSplitter`.
7. **Define the `add_to_chroma()` function:**
    
    - Loads the existing Chroma database.
    - Calculates chunk IDs.
    - Adds or updates documents in the Chroma database.
8. **Define the `calculate_chunk_ids()` function:**
    
    - Calculates chunk IDs based on the source document, page number, and chunk index.
9. **Define the `clear_database()` function:**
    
    - Removes the Chroma database directory if it exists.
10. **Execute the `main()` function:**
    

- Runs the program.

**Key Points:**

- The code loads PDF documents from a specified directory.
- It splits documents into chunks of a specified size.
- It calculates chunk IDs based on the source document, page number, and chunk index.
- It adds or updates documents in a Chroma vector store.
- It provides a command-line option to reset the database


# why there is not an LLM model in these code

**The provided code doesn't explicitly include an LLM model because its primary purpose is to preprocess and store documents in a vector store.**

While the code uses libraries like LangChain, which is often used for building LLM applications, the core functionality here is focused on data preparation and organization. The LLM would typically be used in a separate application or component to interact with the stored documents and generate responses or perform other tasks.

**Here's a breakdown of the code's purpose:**

1. **Load documents:** Reads PDF documents from a specified directory.
2. **Split documents:** Breaks down documents into smaller chunks for easier processing.
3. **Calculate chunk IDs:** Assigns unique identifiers to each chunk.
4. **Store in Chroma:** Stores the document chunks in a Chroma vector store.

**Using an LLM with this code:**

Once the documents are stored in Chroma, an LLM could be used to:

- **Query the vector store:** Search for relevant documents based on a user's query.
- **Generate summaries:** Summarize the contents of specific documents.
- **Answer questions:** Provide answers to questions based on the stored information.
- **Other tasks:** Perform various other language-related tasks as needed.

**In essence, the code provides the foundation for building an LLM-powered application, but the LLM itself would be integrated separately.**


# integrate LLM for these code

To integrate an LLM into the provided code, you'll need to add a component that interacts with the Chroma vector store and uses the LLM to process queries and generate responses. Here's a basic outline of how you could do this:

**1. Choose an LLM:**

- Select an LLM model that suits your needs, such as OpenAI's GPT-3 or a Hugging Face transformer model.

**2. Install the LLM library:**

- Install the required library for the chosen LLM (e.g., `openai`, `transformers`).

**3. Create an LLM instance:**

- Initialize the LLM model with appropriate parameters.

**4. Modify the `add_to_chroma()` function:**

- After adding documents to Chroma, create an LLM-powered chatbot or query interface.
- Use the LLM to process user queries or prompts.
- Query the Chroma vector store to find relevant documents.
- Use the LLM to generate responses based on the retrieved documents.

