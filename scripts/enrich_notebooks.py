"""Rename, move, and add self-learning intros to course notebooks."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MARKER = "**Self-learning notebook**"

NOTEBOOKS: list[dict] = [
    # --- openai-and-prompt-engineering ---
    {
        "src": "openai-and-prompt-engineering/PrompEngineering.ipynb",
        "dst": "openai-and-prompt-engineering/prompt-engineering-guidelines.ipynb",
        "intro": """# Prompt Engineering Guidelines

**Self-learning notebook** — DeepLearning.AI-style prompting principles and tactics.

## What you will learn
- Write clear instructions with delimiters and structured output formats
- Use few-shot examples and chain-of-thought prompting
- Recognize hallucinations and reduce them with better prompts

## Prerequisites
- `OPENAI_API_KEY` in environment or `.env`
- Basic Python and Jupyter/Colab

> Run cells top-to-bottom. Each section builds a prompting tactic you can reuse in production.""",
    },
    {
        "src": "openai-and-prompt-engineering/PrompEngineeringGuideLines.ipynb",
        "dst": "openai-and-prompt-engineering/prompt-engineering-guidelines-copy.ipynb",
        "intro": """# Prompt Engineering Guidelines (Copy)

**Self-learning notebook** — alternate working copy of the main prompting guidelines notebook.

## Note
This notebook mirrors `prompt-engineering-guidelines.ipynb`. Use one as your primary copy; keep this for experiments.

## What you will learn
- Same curriculum: delimiters, structured output, few-shot, chain-of-thought, hallucinations

## Prerequisites
- `OPENAI_API_KEY`""",
    },
    # --- provider-apis (includes moved OpenAI API notebooks) ---
    {
        "src": "openai-and-prompt-engineering/Day2.ipynb",
        "dst": "provider-apis/openai-chat-completions-and-dalle.ipynb",
        "intro": """# OpenAI API: Chat Completions & DALL·E

**Self-learning notebook** — first contact with the OpenAI Python SDK.

## What you will learn
- Configure the `OpenAI` client with an API key from the environment
- Call `chat.completions.create` and read model responses
- Generate images with `client.images.generate` (DALL·E)

## Prerequisites
- `OPENAI_API_KEY`
- Google Colab or local Jupyter with `openai` installed""",
    },
    {
        "src": "openai-and-prompt-engineering/Day3.ipynb",
        "dst": "provider-apis/openai-api-models-and-function-calling.ipynb",
        "intro": """# OpenAI API: Models, Chat & Function Calling

**Self-learning notebook** — explore OpenAI models and structured tool use.

## What you will learn
- List and inspect available OpenAI models programmatically
- Use chat completions with JSON-style structured extraction
- Implement function/tool calling (e.g. weather forecast demo)

## Prerequisites
- `OPENAI_API_KEY`
- `openai`, `pandas`""",
    },
    {
        "src": "openai-and-prompt-engineering/Day3-short.ipynb",
        "dst": "provider-apis/openai-function-calling-short.ipynb",
        "intro": """# OpenAI Function Calling (Short Demo)

**Self-learning notebook** — condensed OpenAI v1 client exercises.

## What you will learn
- Extract structured fields from free text via prompts
- Define custom functions/schemas for tool use
- Compare forced vs optional function invocation

## Prerequisites
- `OPENAI_API_KEY`""",
    },
    {
        "src": "openai-and-prompt-engineering/testopenaiapi_orignal.ipynb",
        "dst": "provider-apis/openai-api-function-calling-original.ipynb",
        "intro": """# OpenAI API & Function Calling (Original)

**Self-learning notebook** — original walkthrough through chat completions and function calling.

## What you will learn
- Set up the OpenAI client and list models
- Use chat completion parameters (`temperature`, `max_tokens`, etc.)
- Structured extraction and function calling basics

## Prerequisites
- `OPENAI_API_KEY`""",
    },
    {
        "src": "openai-and-prompt-engineering/testopenaiapi and langchain (1).ipynb",
        "dst": "provider-apis/openai-api-setup-and-models.ipynb",
        "intro": """# OpenAI API Setup & Model Listing

**Self-learning notebook** — API key setup and model discovery (Part 1 of a longer course).

## What you will learn
- Configure `OPENAI_API_KEY` from environment variables
- List available models with the OpenAI API
- Inspect model metadata with pandas

## Prerequisites
- `OPENAI_API_KEY`""",
    },
    {
        "src": "provider-apis/APIs.ipynb",
        "dst": "scratch/multi-provider-apis-variant.ipynb",
        "intro": """# Multi-Provider APIs (Variant / Scratch)

**Self-learning notebook** — working variant of the Hugging Face + OpenAI + Gemini comparison.

## Note
Canonical copy: `provider-apis/multi-provider-apis-hf-openai-gemini.ipynb`

## What you will learn
- Call Hugging Face Inference API endpoints
- Use OpenAI for chat and image generation
- Authenticate and query Google Gemini""",
    },
    {
        "src": "provider-apis/Huggingface-OpenAI-Gemini.ipynb",
        "dst": "provider-apis/multi-provider-apis-hf-openai-gemini.ipynb",
        "intro": """# Multi-Provider APIs: Hugging Face, OpenAI & Gemini

**Self-learning notebook** — compare open-source and closed LLM APIs side by side.

## What you will learn
- Call HF Inference API (Gemma, Zephyr, Mistral) with `requests`
- Use OpenAI client for chat and image generation
- Authenticate and query Google Gemini API

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN` or HF read token
- `OPENAI_API_KEY`
- `GOOGLE_API_KEY` (Gemini)""",
    },
    # --- langchain ---
    {
        "src": "openai-and-prompt-engineering/Prompts_in_LLMs.ipynb",
        "dst": "langchain/langchain-llama2-prompts-and-chains.ipynb",
        "intro": """# LangChain + Llama 2: Prompts & Chains

**Self-learning notebook** — local Llama-2-7b-chat with LangChain prompt templates.

## What you will learn
- Load gated HF models (`meta-llama/Llama-2-7b-chat-hf`) with authentication
- Wrap a Transformers pipeline in `HuggingFacePipeline`
- Build `PromptTemplate` + `LLMChain` for translation and custom tasks

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN` with Llama 2 access
- GPU recommended (Colab T4 or better)""",
    },
    {
        "src": "openai-and-prompt-engineering/testopenaiapi and langchain (2).ipynb",
        "dst": "langchain/openai-and-langchain-complete-demo.ipynb",
        "intro": """# OpenAI API + LangChain Complete Demo

**Self-learning notebook** — end-to-end OpenAI API and LangChain orchestration.

## What you will learn
- Chat completions and advanced function calling with OpenAI
- LangChain prompt templates, agents, and SerpAPI search
- Simple/sequential chains, document loaders, and memory

## Prerequisites
- `OPENAI_API_KEY`, `SERPAPI_API_KEY` (for search agent sections)""",
    },
    {
        "src": "openai-and-prompt-engineering/testopenaiapi and langchain_orignal.ipynb",
        "dst": "scratch/openai-and-langchain-complete-demo-original.ipynb",
        "intro": """# OpenAI + LangChain Complete Demo (Original Copy)

**Self-learning notebook** — archived original of the combined OpenAI + LangChain course.

## Note
Canonical copy: `langchain/openai-and-langchain-complete-demo.ipynb`""",
    },
    {
        "src": "langchain/LangChain-1.ipynb",
        "dst": "langchain/langchain-openai-zero-shot-intro.ipynb",
        "intro": """# LangChain Intro: OpenAI Zero-Shot Prompting

**Self-learning notebook** — first steps with LangChain's OpenAI wrapper.

## What you will learn
- Initialize LangChain `OpenAI` / `ChatOpenAI` LLM
- Run zero-shot prompts via `predict` / `invoke`
- Explore token usage and conversational prompts

## Prerequisites
- `OPENAI_API_KEY`""",
    },
    {
        "src": "langchain/LangChain-2.ipynb",
        "dst": "langchain/langchain-openai-session-2.ipynb",
        "intro": """# LangChain Session 2: Continued Topics

**Self-learning notebook** — follow-up LangChain session (dated course notes in cells).

## What you will learn
- Extend LangChain patterns from Session 1
- Practice chains, agents, and integrations covered in class

## Prerequisites
- Complete `langchain-openai-zero-shot-intro.ipynb` first
- `OPENAI_API_KEY`""",
    },
    {
        "src": "langchain/Day4.ipynb",
        "dst": "langchain/langchain-openai-prompts-agents-chains.ipynb",
        "intro": """# LangChain: Prompts, Agents, Chains & Memory

**Self-learning notebook** — comprehensive LangChain + OpenAI session.

## What you will learn
- Wrap OpenAI in LangChain `OpenAI` / `ChatOpenAI`
- Build prompt templates and SerpAPI search agents
- Compose chains and conversation buffer memory

## Prerequisites
- `OPENAI_API_KEY`, `SERPAPI_API_KEY`""",
    },
    {
        "src": "langchain/day5.ipynb",
        "dst": "langchain/langchain-openai-prompts-agents-chains-day5.ipynb",
        "intro": """# LangChain Day 5: Prompts, Agents, Chains & Memory

**Self-learning notebook** — alternate session copy of the LangChain + OpenAI curriculum.

## Note
Very similar to `langchain-openai-prompts-agents-chains.ipynb` — use for revision or local edits.

## Prerequisites
- `OPENAI_API_KEY`, `SERPAPI_API_KEY`""",
    },
    {
        "src": "langchain/LangChain_Complete_Course.ipynb",
        "dst": "langchain/langchain-complete-course-openai-hf-gemini.ipynb",
        "intro": """# LangChain Complete Course: OpenAI, Hugging Face & Gemini

**Self-learning notebook** — full LangChain course across multiple LLM providers.

## What you will learn
- LangChain fundamentals with OpenAI, Hugging Face Hub, and Gemini
- Prompt templates, chains, agents, and document loaders
- Multi-provider patterns for production apps

## Prerequisites
- `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`, `GOOGLE_API_KEY`""",
    },
    {
        "src": "langchain/Langchain_HuggingFace_SerpAPI_DocumentLoader_Complete_Demo.ipynb",
        "dst": "langchain/langchain-hf-serpapi-document-loader-demo.ipynb",
        "intro": """# LangChain: Hugging Face, SerpAPI & Document Loaders

**Self-learning notebook** — end-to-end Colab demo of LangChain integrations.

## What you will learn
- Configure LangChain with OpenAI, Hugging Face, and SerpAPI keys
- Build prompt templates, sequential chains, and ReAct agents
- Use conversation memory and `PyPDFLoader` for document chat

## Prerequisites
- Colab secrets: `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`, `SERPAPI_API_KEY`""",
    },
    {
        "src": "langchain/Langchain_HuggingFace_SerpAPI_DocumentLoader_Complete_Demo copy.ipynb",
        "dst": "scratch/langchain-hf-serpapi-demo-copy.ipynb",
        "intro": """# LangChain HF + SerpAPI Demo (Duplicate Copy)

**Self-learning notebook** — archived duplicate.

## Note
Canonical copy: `langchain/langchain-hf-serpapi-document-loader-demo.ipynb`""",
    },
    {
        "src": "langchain/Huggingface_with_Langchain.ipynb",
        "dst": "langchain/langchain-huggingface-hub-and-pipeline.ipynb",
        "intro": """# LangChain + Hugging Face Hub & Local Pipeline

**Self-learning notebook** — seq2seq via Hub API and decoder models locally.

## What you will learn
- Use `HuggingFaceHub` with flan-t5 and mBART seq2seq models
- Compare seq2seq vs decoder-only models in LangChain
- Wrap a local Transformers pipeline with `HuggingFacePipeline`

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`, GPU for local model sections""",
    },
    {
        "src": "langchain/Day5 Hugging face.ipynb",
        "dst": "langchain/langchain-huggingface-setup-day5.ipynb",
        "intro": """# LangChain + Hugging Face Setup (Day 5)

**Self-learning notebook** — Day 5 session: HF Hub chains and local pipeline.

## What you will learn
- Install LangChain + Hugging Face stack in Anaconda/Colab
- Build `PromptTemplate` + `LLMChain` with flan-t5 and mBART
- Load flan-t5 locally via `HuggingFacePipeline`

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`""",
    },
    # --- vector-databases ---
    {
        "src": "vector-databases/FAISS_Demo.ipynb",
        "dst": "vector-databases/faiss-demo-langchain.ipynb",
        "intro": """# FAISS Vector Store with LangChain

**Self-learning notebook** — PDF ingest → embeddings → similarity search → RetrievalQA.

## What you will learn
- Load PDFs with `PyPDFDirectoryLoader` and chunk with `RecursiveCharacterTextSplitter`
- Embed with `HuggingFaceEmbeddings` and build a FAISS index
- Query via `similarity_search` and answer with `RetrievalQA` + OpenAI

## Prerequisites
- `OPENAI_API_KEY`, sample PDFs in a `data/` folder""",
    },
    {
        "src": "vector-databases/FAIIS_Demo_mine.ipynb",
        "dst": "vector-databases/faiss-demo-personal.ipynb",
        "intro": """# FAISS Demo (Personal Variant)

**Self-learning notebook** — personal FAISS + RetrievalQA pipeline.

## Note
Early cells may contain scratch OpenAI image-generation experiments — skip to the FAISS section.

## What you will learn
- Same FAISS pipeline as `faiss-demo-langchain.ipynb`
- Colab secret setup across multiple providers

## Prerequisites
- `OPENAI_API_KEY`, PDF documents for indexing""",
    },
    {
        "src": "vector-databases/ChromaDB_demo.ipynb",
        "dst": "vector-databases/chromadb-demo-langchain.ipynb",
        "intro": """# ChromaDB: Persistence & Semantic Search

**Self-learning notebook** — build, persist, and query a Chroma vector index.

## What you will learn
- Load `.txt` articles and embed with `OpenAIEmbeddings`
- Persist a Chroma index to disk and reload it
- Run semantic search and a `RetrievalQA` chain

## Prerequisites
- `OPENAI_API_KEY`, text documents in a folder""",
    },
    {
        "src": "vector-databases/Weaviate_Vector_Database.ipynb",
        "dst": "vector-databases/weaviate-vector-database-demo.ipynb",
        "intro": """# Weaviate Vector Database Demo

**Self-learning notebook** — cloud Weaviate ingest, embed, search, and chatbot.

## What you will learn
- Connect to Weaviate Cloud and ingest PDFs
- Split, embed (`OpenAIEmbeddings`), and store vectors
- Run similarity search and build a retrieval chatbot

## Prerequisites
- Weaviate cluster URL + API key, `OPENAI_API_KEY`
- Sign up: https://console.weaviate.cloud""",
    },
    {
        "src": "vector-databases/Weaviate_Vector_Database_Mine.ipynb",
        "dst": "vector-databases/weaviate-vector-database-personal.ipynb",
        "intro": """# Weaviate Vector Database (Personal Variant)

**Self-learning notebook** — personal Weaviate cluster configuration.

## What you will learn
- Same ingest → split → embed → store → search flow as the main demo
- Configure your own Weaviate cluster credentials

## Prerequisites
- Personal Weaviate cluster, `OPENAI_API_KEY`""",
    },
    # --- rag-and-chatbots ---
    {
        "src": "rag-and-chatbots/Ineuron_custom_website_chatbot.ipynb",
        "dst": "rag-and-chatbots/ineuron-website-rag-chatbot.ipynb",
        "intro": """# iNeuron Website RAG Chatbot

**Self-learning notebook** — full RAG pipeline for ineuron.ai content.

## What you will learn
- Scrape site pages from sitemap with `UnstructuredURLLoader`
- Chunk text, embed with `sentence-transformers/all-MiniLM-L6-v2`, store in Pinecone
- Run `RetrievalQA` with local Llama-2-7b-chat via `HuggingFacePipeline`

## Prerequisites
- `PINECONE_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`, GPU for Llama 2""",
    },
    {
        "src": "rag-and-chatbots/Ineuron_custom_website_chatbot_mine.ipynb",
        "dst": "rag-and-chatbots/ineuron-website-rag-chatbot-wip.ipynb",
        "intro": """# iNeuron Website RAG Chatbot (Work in Progress)

**Self-learning notebook** — personal WIP: URL extraction only so far.

## Status
Incomplete — stops after document loading. Continue from `ineuron-website-rag-chatbot.ipynb` for the full pipeline.

## What you will learn (so far)
- Install RAG stack (LangChain, Pinecone, transformers)
- Load documents from iNeuron URLs via sitemap""",
    },
    # --- open-source-llms-finetuning ---
    {
        "src": "open-source-llms-finetuning/Open_Source_LLMs_Llama2_(Langchain_&_HuggingFace).ipynb",
        "dst": "open-source-llms-finetuning/llama2-inference-langchain-huggingface.ipynb",
        "intro": """# Llama 2 Inference with LangChain & Hugging Face

**Self-learning notebook** — run Llama 2 7B chat locally via Transformers + LangChain.

## What you will learn
- Load `meta-llama/Llama-2-7b-chat-hf` with bitsandbytes (4-bit optional)
- Build a text-generation pipeline and wrap in `HuggingFacePipeline`
- Prompt for creative naming and Q&A examples

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN` with Llama 2 access, GPU""",
    },
    {
        "src": "open-source-llms-finetuning/Open_Source_LLMs_Llama2_(Langchain_&_HuggingFace)_Mine.ipynb",
        "dst": "open-source-llms-finetuning/llama2-inference-langchain-huggingface-personal.ipynb",
        "intro": """# Llama 2 Inference (Personal Variant)

**Self-learning notebook** — same pipeline using `daryl149/llama-2-7b-chat-hf` (non-gated).

## Note
Compare with `llama2-inference-langchain-huggingface.ipynb` which uses the official gated checkpoint.

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`, GPU""",
    },
    {
        "src": "open-source-llms-finetuning/Mistral_Finetuning_GenaiV1_Mayank.ipynb",
        "dst": "open-source-llms-finetuning/mistral-7b-lora-sft-samsum-mayank.ipynb",
        "intro": """# Mistral 7B LoRA SFT on SAMSum (Mayank)

**Self-learning notebook** — fine-tune GPTQ Mistral for dialogue summarization.

## What you will learn
- Format SAMSum prompts in Human/Assistant style
- Load `TheBloke/Mistral-7B-Instruct-v0.1-GPTQ` with PEFT LoRA
- Train with `SFTTrainer` and push to Hugging Face Hub

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`, GPU (Colab T4+)
- **Security:** rotate any token accidentally saved in notebook outputs before committing""",
    },
    {
        "src": "open-source-llms-finetuning/Mistral_Finetuning_GenaiV1_sunny.ipynb",
        "dst": "open-source-llms-finetuning/mistral-7b-lora-sft-samsum-sunny.ipynb",
        "intro": """# Mistral 7B LoRA SFT on SAMSum (Sunny)

**Self-learning notebook** — parallel Mistral fine-tuning run (50-sample subset).

## What you will learn
- Same SAMSum → instruction formatting → GPTQ Mistral pipeline
- Configure LoRA + `SFTTrainer` for dialogue summarization

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`, GPU""",
    },
    {
        "src": "open-source-llms-finetuning/Finetune_LLM_using_DPO.ipynb",
        "dst": "open-source-llms-finetuning/tinyllama-sft-then-dpo-alignment.ipynb",
        "intro": """# TinyLlama: SFT then DPO Alignment

**Self-learning notebook** — two-stage preference alignment workflow.

## What you will learn
- SFT TinyLlama on Alpaca with 4-bit LoRA (`TrainSFT` helper)
- Apply DPO with `DPOTrainer` on `Anthropic/hh-rlhf` preference pairs
- Load and run the aligned model via pipeline

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`, GPU, `trl`, `peft`, `bitsandbytes`""",
    },
    {
        "src": "open-source-llms-finetuning/Fine_Tune_Llama2_on_Custom_data.ipynb",
        "dst": "open-source-llms-finetuning/llama2-qlora-finetune-guanaco.ipynb",
        "intro": """# Llama 2 QLoRA Fine-Tuning on Guanaco

**Self-learning notebook** — memory-efficient fine-tuning in Colab.

## What you will learn
- Set up QLoRA (4-bit + LoRA) for Colab GPUs
- Fine-tune `NousResearch/Llama-2-7b-chat-hf` on `mlabonne/guanaco-llama2-1k`
- Evaluate, merge LoRA weights, and use TensorBoard

## Prerequisites
- `HUGGINGFACEHUB_API_TOKEN`, Colab GPU (T4; A100 for larger batches)""",
        "skip_intro": True,
    },
    {
        "src": "open-source-llms-finetuning/GGUF_Quantization.ipynb",
        "dst": "open-source-llms-finetuning/gguf-quantization-llama-cpp.ipynb",
        "intro": """# GGUF Quantization with llama.cpp

**Self-learning notebook** — convert HF models to GGUF and run locally.

## What you will learn
- Compare PTQ formats: GPTQ, GGML, GGUF, AWQ
- Build llama.cpp, convert HF → GGUF, apply Q4_K_M quantization
- Run quantized inference and upload artifacts to Hugging Face Hub

## Prerequisites
- Linux/Colab, `cmake`, Hugging Face account""",
    },
    # --- langgraph ---
    {
        "src": "langgraph/LangGraph_Agents_Tools_Memory_Demo.ipynb",
        "dst": "langgraph/langgraph-agents-tools-memory-streaming.ipynb",
        "skip_intro": True,
    },
    {
        "src": "langgraph/LangGraph_Human_in_the_Loop_Interrupt_Demo.ipynb",
        "dst": "langgraph/langgraph-human-in-the-loop-interrupt.ipynb",
        "skip_intro": True,
    },
    # --- huggingface-live-classes ---
    {
        "src": "huggingface-live-classes/Huggingface_Live_Class.ipynb",
        "dst": "huggingface-live-classes/huggingface-hub-api-datasets-inference.ipynb",
        "intro": """# Hugging Face Hub: API, Datasets & Inference (Live Class)

**Self-learning notebook** — comprehensive HF Hub exploration from live class (30 May 2026).

## What you will learn
- Use `HfApi` for model info, search, repo create/upload
- Load WikiText and Alpaca datasets; run `InferenceClient`
- Optional LangChain Hugging Face endpoint integration

## Prerequisites
- HF read + write tokens in Colab secrets""",
    },
    {
        "src": "huggingface-live-classes/huggingface_explore_live_class-24May26.ipynb",
        "dst": "scratch/huggingface-hub-explore-2025-05-24.ipynb",
        "intro": """# Hugging Face Hub Explore (24 May 2026 Draft)

**Self-learning notebook** — early draft of the live-class material.

## Note
Canonical copy: `huggingface-live-classes/huggingface-hub-api-datasets-inference.ipynb`""",
    },
    {
        "src": "huggingface-live-classes/Huggingface_explore_live_class-25May26.ipynb",
        "dst": "scratch/huggingface-hub-explore-2025-05-25.ipynb",
        "intro": """# Hugging Face Hub Explore (25 May 2026 Draft)

**Self-learning notebook** — short token-discovery draft.

## Note
Superseded by the full live-class notebook in `huggingface-live-classes/`.""",
    },
    # --- scratch ---
    {
        "src": "scratch/Untitled.ipynb",
        "dst": "scratch/openai-api-pathlib-experiments.ipynb",
        "intro": """# OpenAI API & Pathlib Experiments (Scratch)

**Self-learning notebook** — ad-hoc local experiments, not part of the guided course path.

## Contents
- `pathlib` and environment variable probing
- OpenAI chat completion attempts (may show auth errors in saved outputs)""",
    },
    {
        "src": "scratch/Untitled2.ipynb",
        "dst": "scratch/tensorflow-install-troubleshooting.ipynb",
        "intro": """# TensorFlow Install Troubleshooting (Scratch)

**Self-learning notebook** — debugging TensorFlow import issues on macOS conda.

## Contents
- Failed `import tensorflow` attempts and dependency errors
- pip install variants (`tensorflow==2.12.0`, `tensorflow-macos`)""",
    },
]

SETUP_COMMENT = "# Setup: install dependencies for this section (run once per session)\n"


def load_notebook(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_notebook(path: Path, nb: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")


def has_self_learning_intro(nb: dict) -> bool:
    for cell in nb.get("cells", [])[:3]:
        if cell.get("cell_type") != "markdown":
            continue
        source = "".join(cell.get("source", []))
        if MARKER in source:
            return True
    return False


def make_markdown_cell(text: str) -> dict:
    lines = text.strip().split("\n")
    source = [line + "\n" for line in lines[:-1]]
    if lines:
        source.append(lines[-1])
    return {"cell_type": "markdown", "metadata": {}, "source": source}


def prepend_intro(nb: dict, intro: str) -> None:
    if has_self_learning_intro(nb):
        return
    nb["cells"].insert(0, make_markdown_cell(intro))


def annotate_first_pip_cells(nb: dict) -> None:
    seen_pip = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", [])
        if not source:
            continue
        first = source[0] if isinstance(source, list) else source
        text = first if isinstance(first, str) else ""
        if "!pip install" in text or "pip install" in text:
            if not text.strip().startswith("#"):
                if isinstance(source, list):
                    cell["source"] = [SETUP_COMMENT + text] + source[1:]
                seen_pip = True
        elif seen_pip:
            break


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        raise FileNotFoundError(src)
    if dst.exists():
        raise FileExistsError(dst)
    try:
        subprocess.run(
            ["git", "mv", str(src), str(dst)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        shutil.move(str(src), str(dst))


def process_entry(entry: dict) -> str:
    src = ROOT / entry["src"]
    dst = ROOT / entry["dst"]
    if not src.exists():
        return f"SKIP missing: {entry['src']}"

    nb = load_notebook(src)
    if not entry.get("skip_intro") and entry.get("intro"):
        prepend_intro(nb, entry["intro"])
    annotate_first_pip_cells(nb)
    save_notebook(src, nb)

    if src.resolve() != dst.resolve():
        git_mv(src, dst)
        return f"OK {entry['src']} -> {entry['dst']}"
    return f"OK enriched: {entry['dst']}"


def main() -> None:
    results = [process_entry(e) for e in NOTEBOOKS]
    for line in results:
        print(line)
    expected = {ROOT / e["dst"] for e in NOTEBOOKS}
    actual = set(ROOT.rglob("*.ipynb"))
    unmapped = sorted(actual - expected)
    if unmapped:
        print("\nUnmapped notebooks:")
        for p in unmapped:
            print(f"  {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
