# Notebooks: Fine-Tuning LLMs, Hugging Face, Vector DBs, and RAG

A notebook-only learning repository for building with large language models: prompt design, LangChain orchestration, retrieval-augmented generation (RAG), vector databases, and fine-tuning or alignment workflows. Most notebooks target Google Colab (GPU where needed) and load API keys from environment variables or a local `.env` file.

## What is in this repository

- **42 Jupyter notebooks** organized into topic folders; each includes a **self-learning intro** (objectives, prerequisites) at the top.
- **Course-style progression** from `provider-apis/openai-chat-completions-and-dalle.ipynb` through `langchain/langchain-huggingface-setup-day5.ipynb`, plus LangGraph and fine-tuning tracks.
- **Personal or duplicate variants** kept with clear names (`-personal`, `-copy`, `-wip`, `-mayank`, `-sunny`); archived copies live in `scratch/`.
- **Scratch notebooks** in `scratch/` — drafts, duplicates, and experiments not on the guided path.

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

Each notebook opens with a self-learning markdown cell: title, learning objectives, and prerequisites. Run cells top-to-bottom.

### `openai-and-prompt-engineering/` (2)

| Notebook | Focus |
| --- | --- |
| `prompt-engineering-guidelines.ipynb` | Prompting principles: delimiters, structured output, few-shot, chain-of-thought, hallucinations |
| `prompt-engineering-guidelines-copy.ipynb` | Alternate working copy of the guidelines notebook |

### `provider-apis/` (7)

| Notebook | Focus |
| --- | --- |
| `openai-chat-completions-and-dalle.ipynb` | First OpenAI SDK: chat completions and DALL·E image generation |
| `openai-api-models-and-function-calling.ipynb` | Model listing, chat completions, JSON extraction, function calling |
| `openai-function-calling-short.ipynb` | Condensed function-calling and structured extraction demo |
| `openai-api-function-calling-original.ipynb` | Original OpenAI API + function calling walkthrough |
| `openai-api-setup-and-models.ipynb` | API key setup and model discovery (Part 1 of longer course) |
| `multi-provider-apis-hf-openai-gemini.ipynb` | Hugging Face Inference, OpenAI GPT, and Google Gemini comparison |

### `langchain/` (11)

| Notebook | Focus |
| --- | --- |
| `langchain-openai-zero-shot-intro.ipynb` | LangChain intro with OpenAI zero-shot prompting |
| `langchain-openai-session-2.ipynb` | Continued LangChain session topics |
| `langchain-openai-prompts-agents-chains.ipynb` | Prompts, SerpAPI agents, chains, memory |
| `langchain-openai-prompts-agents-chains-day5.ipynb` | Day 5 alternate copy of the agents/chains session |
| `langchain-complete-course-openai-hf-gemini.ipynb` | Full LangChain course across OpenAI, HF Hub, and Gemini |
| `openai-and-langchain-complete-demo.ipynb` | Combined OpenAI API + LangChain end-to-end demo |
| `langchain-hf-serpapi-document-loader-demo.ipynb` | HF Hub, SerpAPI, document loaders, agents, memory |
| `langchain-huggingface-hub-and-pipeline.ipynb` | HuggingFaceHub seq2seq + local HuggingFacePipeline |
| `langchain-huggingface-setup-day5.ipynb` | Day 5 Hugging Face + LangChain environment setup |
| `langchain-llama2-prompts-and-chains.ipynb` | Local Llama 2 with LangChain prompts and LLMChain |

### `vector-databases/` (5)

| Notebook | Focus |
| --- | --- |
| `faiss-demo-langchain.ipynb` | FAISS vector store: PDF ingest, embeddings, RetrievalQA |
| `faiss-demo-personal.ipynb` | Personal FAISS variant |
| `chromadb-demo-langchain.ipynb` | Chroma persistence, semantic search, RetrievalQA |
| `weaviate-vector-database-demo.ipynb` | Weaviate cloud: ingest, embed, search, chatbot |
| `weaviate-vector-database-personal.ipynb` | Personal Weaviate cluster variant |

### `rag-and-chatbots/` (2)

| Notebook | Focus |
| --- | --- |
| `ineuron-website-rag-chatbot.ipynb` | Full RAG chatbot: sitemap scrape, Pinecone, Llama 2 RetrievalQA |
| `ineuron-website-rag-chatbot-wip.ipynb` | Work-in-progress personal variant (URL extraction only) |

### `open-source-llms-finetuning/` (7)

| Notebook | Focus |
| --- | --- |
| `llama2-inference-langchain-huggingface.ipynb` | Llama 2 7B inference via Transformers + LangChain |
| `llama2-inference-langchain-huggingface-personal.ipynb` | Personal variant using non-gated Llama 2 checkpoint |
| `mistral-7b-lora-sft-samsum-mayank.ipynb` | Mistral 7B GPTQ + LoRA SFT on SAMSum (Mayank) |
| `mistral-7b-lora-sft-samsum-sunny.ipynb` | Parallel Mistral SFT run (Sunny) |
| `tinyllama-sft-then-dpo-alignment.ipynb` | SFT on Alpaca, then DPO on Anthropic HH-RLHF |
| `llama2-qlora-finetune-guanaco.ipynb` | QLoRA fine-tuning Llama 2 on Guanaco instruction data |
| `gguf-quantization-llama-cpp.ipynb` | GGUF quantization with llama.cpp and Hub upload |

### `langgraph/` (2)

| Notebook | Focus |
| --- | --- |
| `langgraph-agents-tools-memory-streaming.ipynb` | StateGraph agents, tools, ReAct loop, checkpoint memory, streaming |
| `langgraph-human-in-the-loop-interrupt.ipynb` | Human-in-the-loop `interrupt()` and `Command(resume=...)` |

### `huggingface-live-classes/` (1)

| Notebook | Focus |
| --- | --- |
| `huggingface-hub-api-datasets-inference.ipynb` | HF Hub API, datasets (WikiText, Alpaca), InferenceClient |

### `scratch/` (7)

| Notebook | Notes |
| --- | --- |
| `multi-provider-apis-variant.ipynb` | Duplicate of multi-provider APIs notebook |
| `openai-and-langchain-complete-demo-original.ipynb` | Archived original of combined OpenAI + LangChain demo |
| `langchain-hf-serpapi-demo-copy.ipynb` | Duplicate of SerpAPI document-loader demo |
| `huggingface-hub-explore-2025-05-24.ipynb` | Early draft of live-class material |
| `huggingface-hub-explore-2025-05-25.ipynb` | Short token-discovery draft |
| `openai-api-pathlib-experiments.ipynb` | Ad-hoc OpenAI and pathlib experiments |
| `tensorflow-install-troubleshooting.ipynb` | TensorFlow install debugging on macOS |

## Suggested learning path

1. **Prompts** — `openai-and-prompt-engineering/prompt-engineering-guidelines.ipynb`
2. **APIs** — `provider-apis/openai-api-models-and-function-calling.ipynb`, then `provider-apis/multi-provider-apis-hf-openai-gemini.ipynb`
3. **LangChain core** — `langchain/langchain-openai-zero-shot-intro.ipynb` → `langchain/langchain-hf-serpapi-document-loader-demo.ipynb`
4. **Embeddings & retrieval** — `vector-databases/faiss-demo-langchain.ipynb` or `vector-databases/chromadb-demo-langchain.ipynb` → `vector-databases/weaviate-vector-database-demo.ipynb`
5. **RAG application** — `rag-and-chatbots/ineuron-website-rag-chatbot.ipynb`
6. **LangGraph** — `langgraph/langgraph-agents-tools-memory-streaming.ipynb` → `langgraph/langgraph-human-in-the-loop-interrupt.ipynb`
7. **Open weights & training** — `open-source-llms-finetuning/llama2-inference-langchain-huggingface.ipynb` → `open-source-llms-finetuning/mistral-7b-lora-sft-samsum-mayank.ipynb` → `open-source-llms-finetuning/tinyllama-sft-then-dpo-alignment.ipynb` → `open-source-llms-finetuning/gguf-quantization-llama-cpp.ipynb`

## Tools and libraries

Python, Jupyter, Google Colab, LangChain, Hugging Face Transformers / Datasets / PEFT / TRL, PyTorch, FAISS, ChromaDB, Weaviate, Pinecone, OpenAI API, Google Gemini API, SerpAPI, and dotenv-based configuration.

## Troubleshooting

| Guide | When to use it |
| --- | --- |
| [github-troubleshooting.md](github-troubleshooting.md) | Push blocked (GH013), secrets in notebook outputs or git history, rotating compromised tokens |

## License

MIT License. Copyright (c) 2024 Mayank Chugh. See [LICENSE](LICENSE).
