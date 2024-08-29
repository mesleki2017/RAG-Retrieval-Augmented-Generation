from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from langchain_community.embeddings import SentenceTransformerEmbeddings
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import StorageContext, load_index_from_storage

Settings.llm = Ollama(model="llama3", request_timeout=120.0)
Settings.embed_model =SentenceTransformerEmbeddings(model_name='C://Users//bulent.cesur//Documents//all-MiniLM-L6-v2')
required_exts = [".docx",".pdf"]
documents = SimpleDirectoryReader("data", required_exts=required_exts,
    recursive=False,).load_data()


Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
Settings.num_output = 512
Settings.context_window = 3900



if True:
    storage_context = StorageContext.from_defaults(persist_dir="myllamaindex")
    index = load_index_from_storage(storage_context)
if False:
    index = VectorStoreIndex.from_documents(
        documents
    )
    index.storage_context.persist(persist_dir="myllamaindex")

query_engine = index.as_query_engine()
response = query_engine.query("kablo çeşitleri nelerdir?")

print(response)
