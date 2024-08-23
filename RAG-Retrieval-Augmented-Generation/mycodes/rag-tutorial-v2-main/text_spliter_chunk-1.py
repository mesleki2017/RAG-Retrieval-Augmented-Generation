from langchain_community.document_loaders import PyPDFDirectoryLoader

docs = PyPDFDirectoryLoader("data").load()


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

chunks = split_documents(docs)



for chunk in chunks:
    print(chunk)