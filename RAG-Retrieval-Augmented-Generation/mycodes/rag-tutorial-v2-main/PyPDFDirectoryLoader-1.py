from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.schema.document import Document


docs = PyPDFDirectoryLoader("data").load()

for doc in docs:
    print(doc.page_content)