# Data

The full scraped corpus is intentionally not distributed in this repository.

Generate compatible JSONL files with the collection scripts in this directory. The chunking notebooks expect these filenames:

- `corpus_wikipedia.jsonl`
- `corpus_wikibooks_east_asia.jsonl`
- `corpus_blog.jsonl`

Each record should contain a stable `doc_id`, source metadata, a title, and a text/body field. Review each source's licence, robots policy, and terms of use before collecting or redistributing content.
