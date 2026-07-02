import json
from pathlib import Path

from langchain_core.documents import Document


def load_catalog():
    catalog_path = Path(__file__).with_name("catalog.json")
    raw_bytes = catalog_path.read_bytes()

    for encoding in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return json.loads(raw_bytes.decode(encoding))
        except UnicodeDecodeError:
            continue
        except json.JSONDecodeError:
            continue

    return json.loads(raw_bytes.decode("utf-8", errors="replace"))


catalog = load_catalog()
docs = []


def build_docs():
    for item in catalog:

        doc = Document(
            page_content=f"""
            Assessment Name: {item['name']}

            Description:
            {item['description']}

            Job Levels:
            {', '.join(item['job_levels'])}

            Categories:
            {', '.join(item['keys'])}
            """,

            metadata={
                "name": item["name"],
                "url": item["link"],
                "test_type": item["keys"]
            }
        )
        docs.append(doc)
    return docs


