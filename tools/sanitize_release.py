"""Remove notebook outputs and machine-specific paths from the release copy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def clean_notebook(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None

        source = "".join(cell.get("source", []))
        source = source.replace("../chuncking/", "../chunking/")
        cell["source"] = source.splitlines(keepends=True)

    metadata = notebook.setdefault("metadata", {})
    metadata.pop("widgets", None)
    path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def clean_result_paths(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))

    def visit(value):
        if isinstance(value, dict):
            for key, item in list(value.items()):
                if key in {"retrieval_path", "output_path"} and isinstance(item, str):
                    value[key] = Path(item.replace("\\", "/")).name
                else:
                    visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(payload)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    notebooks = sorted(ROOT.rglob("*.ipynb"))
    for notebook in notebooks:
        clean_notebook(notebook)

    for result in sorted((ROOT / "results").glob("*.json")):
        clean_result_paths(result)

    print(f"Cleaned {len(notebooks)} notebooks and release result paths.")


if __name__ == "__main__":
    main()
