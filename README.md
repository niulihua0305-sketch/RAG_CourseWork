# East Asian Cuisine RAG Pipeline

An experimental retrieval-augmented generation (RAG) system for question answering about East Asian cuisine. The project compares chunking strategies, embedding models, bi-encoder retrieval, cross-encoder reranking, prompt designs, and generation settings in one reproducible workflow.

## Pipeline

```text
Web sources
    -> corpus collection and cleaning
    -> fixed, sentence, or structure-aware chunking
    -> MiniLM or Nomic embeddings + FAISS
    -> bi-encoder retrieval
    -> optional cross-encoder reranking
    -> Qwen2.5-0.5B-Instruct generation
    -> retrieval and answer evaluation
```

## Main experiments

- **Chunking:** fixed 300-token windows, sentence-based chunks with overlap, and structure-aware chunks.
- **Embeddings:** `all-MiniLM-L6-v2`, `nomic-ai/nomic-embed-text-v1.5`, and an optional OpenAI baseline.
- **Retrieval:** top-5/top-20 dense retrieval with optional `ms-marco-MiniLM-L-6-v2` reranking.
- **Generation:** basic, enhanced, chain-of-thought, and few-shot prompts evaluated under several decoding settings.
- **Metrics:** Hit@1, Hit@5, Recall@20, MRR, token-level F1, ROUGE, and BERTScore.

The saved experiment summaries show that the strongest recorded retrieval configurations reached **Hit@5 = 0.967** and **Recall@20 = 0.983** on the 60-question benchmark. For generation, the strongest saved token-level result used the basic prompt at temperature 0.3, with **F1 = 0.414** and **ROUGE-L F1 = 0.369**. These figures describe the saved coursework experiments rather than a newly reproduced run.

## Repository layout

```text
data/          corpus collection and cleaning scripts; benchmark metadata
chunking/      three chunking notebooks
embedding/     local embedding and FAISS-index construction
retrieval/     retrieval, reranking, and retrieval evaluation
generation/    answer generation and generation evaluation
examples/      small input examples
results/       compact experiment summaries
tools/         release-cleaning utility
```

Large corpora, generated embeddings, FAISS indices, model caches, and full per-query outputs are intentionally excluded from version control.

## Setup

Python 3.10 is recommended.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
```

The default local pipeline does not require an API key. Optional services use environment variables only:

```bash
copy .env.example .env
```

Do not commit `.env` or place credentials directly in notebooks or scripts.

## Running the workflow

1. Generate the source corpora with the scripts in `data/`, or place compatible JSONL corpora there.
2. Run one or more notebooks in `chunking/`. Generated chunks are written to `chunking/data/`.
3. Run `embedding/chunk_embedding.ipynb`. The local Nomic configuration is the recommended default; indices are written to `embedding/output/`.
4. Run `retrieval/03_retrieval_v2_2.ipynb` for the main retrieval experiment, or use `retrieval/run_retrieval_models.py` for batch comparisons.
5. Run `generation/inference.ipynb`, followed by `generation/generation_evaluation.ipynb`.

Notebooks use paths relative to their own directories, so start Jupyter from the repository root and open the notebook in its original folder.

## Data and reproducibility notes

- The repository includes the benchmark schema and small query examples, but not the full scraped corpus or generated vector stores.
- Model downloads and corpus regeneration require internet access.
- Third-party source content remains subject to its original licence and terms of use.
- Exact numerical reproduction may vary with package/model versions and hardware.

## Attribution

This is a cleaned portfolio version of a team coursework project for the University of Manchester course *Transforming Text into Meaning*. The original development history includes contributions from multiple team members. Before making this repository public, confirm that all contributors agree and that publication is consistent with the course's academic-integrity policy.

No licence is granted by default. Add a licence only after confirming ownership and contributor permission.
