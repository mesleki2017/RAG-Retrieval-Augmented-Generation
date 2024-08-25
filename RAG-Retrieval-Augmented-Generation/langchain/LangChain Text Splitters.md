#langchain 

Once you've loaded documents, you'll often want to transform them to better suit your application. The simplest example is you may want to split a long document into smaller chunks that can fit into your model's context window. LangChain has a number of built-in document transformers that make it easy to split, combine, filter, and otherwise manipulate documents.

When you want to deal with long pieces of text, it is necessary to split up that text into chunks. As simple as this sounds, there is a lot of potential complexity here. Ideally, you want to keep the semantically related pieces of text together. What "semantically related" means could depend on the type of text. This notebook showcases several ways to do that.

At a high level, text splitters work as following:

1. Split the text up into small, semantically meaningful chunks (often sentences).
2. Start combining these small chunks into a larger chunk until you reach a certain size (as measured by some function).
3. Once you reach that size, make that chunk its own piece of text and then start creating a new chunk of text with some overlap (to keep context between chunks).

That means there are two different axes along which you can customize your text splitter:

1. How the text is split
2. How the chunk size is measured


| Name      | Classes                                                                                                                                                                                                                                                                                 | Splits On                         | Adds Metadata | Description                                                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recursive | [RecursiveCharacterTextSplitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/), [RecursiveJsonSplitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_json_splitter/) | A list of user defined characters |               | Recursively splits text. This splitting is trying to keep related pieces of text next to each other. This is the `recommended way` to start splitting text. |

https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/