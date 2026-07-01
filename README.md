# Notebooks: Fine-Tuning LLMs, Hugging Face, Vector DBs, and RAG

A notebook-only learning repository for building with large language models: prompt design, LangChain orchestration, retrieval-augmented generation (RAG), vector databases, and fine-tuning or alignment workflows. Most notebooks target Google Colab (GPU where needed) and load API keys from environment variables or a local `.env` file.

## What is in this repository

- **42 Jupyter notebooks** organized into topic folders; there is no packaged Python application or shared library layer.
- **Course-style progression** in `openai-and-prompt-engineering/Day2.ipynb` through `langchain/Day5 Hugging face.ipynb`, plus parallel LangChain walkthroughs and end-to-end demos.
- **Personal or duplicate variants** of several notebooks, often suffixed with `_Mine`, `_orignal`, or `(1)` / `(2)`, for side-by-side comparison or scratch work.
- **Scratch notebooks** (`Untitled.ipynb`, `Untitled2.ipynb`) that are not part of a guided path.

## Topics covered

| Area | What you will practice |
| --- | --- |
| OpenAI and prompting | API setup, playground-style usage, structured prompting, and hallucination awareness |
| Multi-provider APIs | Hugging Face Inference, OpenAI GPT, Google Gemini / Gemma, and related REST patterns |
| LangChain | Prompt templates, chains, agents, tools, memory, and document loaders |
| LangGraph | Stateful agents, human-in-the-loop interrupts, tools, and memory |
| RAG | URL ingestion, chunking, embeddings, vector retrieval, and Q&A chains |
| Vector stores | FAISS, ChromaDB, Weaviate, and Pinecone |
| Open models | LLaMA 2 and Mistral with Hugging Face Transformers and LangChain wrappers |
| Training and alignment | LoRA / PEFT, supervised fine-tuning (SFT), and Direct Preference Optimization (DPO) |
| Deployment efficiency | GGUF and related quantization concepts with `llama.cpp` / Hugging Face Hub workflows |

## Getting started

1. Clone the repository and open a notebook in Jupyter, VS Code, or [Google Colab](https://colab.research.google.com/) (many notebooks include an Open in Colab badge).
2. Create a `.env` file in the project root (see `.gitignore`; secrets are not committed). Common variables used across notebooks:
   - `OPENAI_API_KEY`
   - `GOOGLE_API_KEY`
   - `HUGGINGFACE_TOKEN` or `HUGGINGFACEHUB_API_TOKEN`
   - Provider-specific keys such as SerpAPI, Pinecone, or Weaviate cluster URL and API key when a notebook calls those services
3. Install dependencies per notebook (`pip install` cells). Stacks vary by topic; expect **LangChain**, **Hugging Face** (`transformers`, `datasets`, `peft`, `trl`, `accelerate`), **PyTorch**, and vector-database clients.
4. Prefer a **GPU runtime** for fine-tuning, embedding at scale, and large open-weight model loading.
5. Before pushing notebooks, clear cell outputs so API keys are not saved in the `.ipynb` file. If GitHub rejects a push for leaked secrets, see [github-troubleshooting.md](github-troubleshooting.md).

## Notebook index

Notebooks are grouped by topic in the folders below.

### `openai-and-prompt-engineering/`

| Notebook | Focus |
| --- | --- |
| `Day2.ipynb` | Early OpenAI API usage |
| `Day3.ipynb` | OpenAI API overview, key generation, and playground-style exploration |
| `Day3-short.ipynb` | Shorter OpenAI API exercises |
| `testopenaiapi_orignal.ipynb` | OpenAI API walkthrough (original variant) |
| `testopenaiapi and langchain_orignal.ipynb` | OpenAI API with LangChain (original variant) |
| `testopenaiapi and langchain (1).ipynb` | OpenAI API with LangChain (variant 1) |
| `testopenaiapi and langchain (2).ipynb` | OpenAI API with LangChain (variant 2) |
| `PrompEngineering.ipynb` | Prompting guidelines: delimiters, structured output, few-shot, and chain-of-thought tactics |
| `PrompEngineeringGuideLines.ipynb` | Same prompting curriculum (alternate copy) |
| `Prompts_in_LLMs.ipynb` | Prompt patterns in LLM workflows, including translation-style tasks |

### `provider-apis/`

| Notebook | Focus |
| --- | --- |
| `APIs.ipynb` | Hugging Face Inference API, Gemma, OpenAI GPT, and Gemini |
| `Huggingface-OpenAI-Gemini.ipynb` | Multi-provider API comparison and usage |

### `langchain/`

| Notebook | Focus |
| --- | --- |
| `LangChain-1.ipynb` | LangChain basics: prompts, agents, chains, memory, document loaders |
| `LangChain-2.ipynb` | Continued LangChain topics (dated session notes in notebook) |
| `day5.ipynb` | LangChain session: prompting, agents, SerpAPI, chains, memory |
| `Day4.ipynb` | Prompt templates and agents |
| `LangChain_Complete_Course.ipynb` | LangChain with OpenAI, Hugging Face Hub, and Gemini |
| `Langchain_HuggingFace_SerpAPI_DocumentLoader_Complete_Demo.ipynb` | End-to-end LangChain demo: Hugging Face, SerpAPI, loaders, agents, memory |
| `Langchain_HuggingFace_SerpAPI_DocumentLoader_Complete_Demo copy.ipynb` | Duplicate of the complete LangChain demo |
| `Huggingface_with_Langchain.ipynb` | Hugging Face models integrated with LangChain |
| `Day5 Hugging face.ipynb` | Hugging Face + LangChain setup and environment configuration |

### `vector-databases/`

| Notebook | Focus |
| --- | --- |
| `FAISS_Demo.ipynb` | FAISS vector store with LangChain |
| `FAIIS_Demo_mine.ipynb` | Personal FAISS variant |
| `ChromaDB_demo.ipynb` | Chroma persistence, semantic search, and chaining |
| `Weaviate_Vector_Database.ipynb` | Weaviate: ingest, split, embed, and store vectors |
| `Weaviate_Vector_Database_Mine.ipynb` | Personal Weaviate variant |

### `rag-and-chatbots/`

| Notebook | Focus |
| --- | --- |
| `Ineuron_custom_website_chatbot.ipynb` | Website URL ingestion, chunking, Pinecone, embeddings, retrieval Q&A |
| `Ineuron_custom_website_chatbot_mine.ipynb` | Personal variant (URL extraction and RAG setup) |

### `open-source-llms-finetuning/`

| Notebook | Focus |
| --- | --- |
| `Open_Source_LLMs_Llama2_(Langchain_&_HuggingFace).ipynb` | LLaMA 2 with LangChain and Hugging Face |
| `Open_Source_LLMs_Llama2_(Langchain_&_HuggingFace)_Mine.ipynb` | Personal LLaMA 2 variant |
| `Mistral_Finetuning_GenaiV1_Mayank.ipynb` | Mistral SFT on `samsum` with PEFT / `SFTTrainer` |
| `Mistral_Finetuning_GenaiV1_sunny.ipynb` | Parallel Mistral fine-tuning notebook |
| `Finetune_LLM_using_DPO.ipynb` | SFT then DPO alignment (Alpaca, Anthropic HH-RLHF, LoRA, `DPOTrainer`) |
| `Fine_Tune_Llama2_on_Custom_data.ipynb` | LLaMA 2 fine-tuning on custom data |
| `GGUF_Quantization.ipynb` | Quantization formats (GPTQ, GGML, GGUF, AWQ) and `llama.cpp` / Hub download notes |

### `langgraph/`

| Notebook | Focus |
| --- | --- |
| `LangGraph_Agents_Tools_Memory_Demo.ipynb` | LangGraph agents with tools and memory |
| `LangGraph_Human_in_the_Loop_Interrupt_Demo.ipynb` | Human-in-the-loop interrupts with LangGraph |

### `huggingface-live-classes/`

| Notebook | Focus |
| --- | --- |
| `Huggingface_Live_Class.ipynb` | Hugging Face live class session |
| `huggingface_explore_live_class-24May26.ipynb` | Hugging Face explore session (24 May 2026) |
| `Huggingface_explore_live_class-25May26.ipynb` | Hugging Face explore session (25 May 2026) |

### `scratch/`

| Notebook | Notes |
| --- | --- |
| `Untitled.ipynb` | Minimal OpenAI / path experiments |
| `Untitled2.ipynb` | TensorFlow scratch |

## Suggested learning path

1. **APIs and prompts** — `openai-and-prompt-engineering/Day3.ipynb` or `openai-and-prompt-engineering/PrompEngineering.ipynb`, then `provider-apis/APIs.ipynb` or `provider-apis/Huggingface-OpenAI-Gemini.ipynb`.
2. **LangChain core** — `langchain/LangChain-1.ipynb` and `langchain/Langchain_HuggingFace_SerpAPI_DocumentLoader_Complete_Demo.ipynb`.
3. **Embeddings and retrieval** — `vector-databases/FAISS_Demo.ipynb` or `vector-databases/ChromaDB_demo.ipynb`, then `vector-databases/Weaviate_Vector_Database.ipynb`.
4. **RAG application** — `rag-and-chatbots/Ineuron_custom_website_chatbot.ipynb`.
5. **Open weights and training** — `open-source-llms-finetuning/Open_Source_LLMs_Llama2_(Langchain_&_HuggingFace).ipynb`, `open-source-llms-finetuning/Mistral_Finetuning_GenaiV1_Mayank.ipynb`, `open-source-llms-finetuning/Finetune_LLM_using_DPO.ipynb`, and `open-source-llms-finetuning/GGUF_Quantization.ipynb` as needed.

## Tools and libraries

Python, Jupyter, Google Colab, LangChain, Hugging Face Transformers / Datasets / PEFT / TRL, PyTorch, FAISS, ChromaDB, Weaviate, Pinecone, OpenAI API, Google Gemini API, SerpAPI, and dotenv-based configuration.

## Troubleshooting

| Guide | When to use it |
| --- | --- |
| [github-troubleshooting.md](github-troubleshooting.md) | Push blocked (GH013), secrets in notebook outputs or git history, rotating compromised tokens |

## License

MIT License. Copyright (c) 2024 Mayank Chugh. See [LICENSE](LICENSE).
