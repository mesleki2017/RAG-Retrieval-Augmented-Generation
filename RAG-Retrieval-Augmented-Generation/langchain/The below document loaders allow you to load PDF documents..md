|Document Loader|Description|Package/API|
|---|---|---|
|[PyPDF](https://python.langchain.com/v0.2/docs/integrations/document_loaders/pypdfloader)|Uses `pypdf` to load and parse PDFs|Package|
|[Unstructured](https://python.langchain.com/v0.2/docs/integrations/document_loaders/unstructured_file)|Uses Unstructured's open source library to load PDFs|Package|
|[Amazon Textract](https://python.langchain.com/v0.2/docs/integrations/document_loaders/amazon_textract)|Uses AWS API to load PDFs|API|
|[MathPix](https://python.langchain.com/v0.2/docs/integrations/document_loaders/mathpix)|Uses MathPix to laod PDFs|Package|
|[PDFPlumber](https://python.langchain.com/v0.2/docs/integrations/document_loaders/pdfplumber)|Load PDF files using PDFPlumber|Package|
|[PyPDFDirectry](https://python.langchain.com/v0.2/docs/integrations/document_loaders/pypdfdirectory)|Load a directory with PDF files|Package|
|[PyPDFium2](https://python.langchain.com/v0.2/docs/integrations/document_loaders/pypdfium2)|Load PDF files using PyPDFium2|Package|
|[UnstructuredPDFLoader](https://python.langchain.com/v0.2/docs/integrations/document_loaders/unstructured_pdfloader)|Load PDF files using Unstructured|Package|
|[PyMuPDF](https://python.langchain.com/v0.2/docs/integrations/document_loaders/pymupdf)|Load PDF files using PyMuPDF|Package|
|[PDFMiner](https://python.langchain.com/v0.2/docs/integrations/document_loaders/pdfminer)|Load PDF files using PDFMiner|Package|


https://python.langchain.com/v0.2/docs/integrations/document_loaders/pypdfdirectory/
```python
from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader("data")
docs = loader.load()
print(docs[0].metadata)
```
```
{'source': 'data\\cccc.pdf', 'page': 0}
```
