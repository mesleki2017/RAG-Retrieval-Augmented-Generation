### Using a local LLM[#](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/#using-a-local-llm "Permanent link")

LlamaIndex doesn't just support hosted LLM APIs; you can also [run a local model such as Llama2 locally](https://replicate.com/blog/run-llama-locally).

For example, if you have [Ollama](https://github.com/ollama/ollama) installed and running:

```python
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

Settings.llm = Ollama(model="llama2", request_timeout=60.0)

```
