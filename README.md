# SHL Assessment Recommendation Assistant

A Python-based recommendation system that uses a structured LLM, semantic search, and SHL product catalog embeddings to recommend relevant assessments based on hiring conversation context.

## What this project does

- Builds searchable document embeddings from an SHL assessment catalog (`catalog.json`).
- Extracts structured hiring requirements from user conversation using a Groq-based language model.
- Generates a semantic search query from the extracted requirements.
- Uses a tool-enabled agent to search the catalog and recommend assessments.
- Exposes a small FastAPI endpoint for health checks and chat responses.

## Key components

- `main.py` - primary orchestration flow for conversation processing and agent invocation.
- `agent.py` - defines the Groq chat model, agent prompt, and tools available to the agent.
- `Vector_store.py` - builds a Chroma vector store from catalog documents.
- `docs_builder.py` - loads `catalog.json` and converts items into LangChain `Document` objects.
- `utils/functions.py` - extracts hiring requirements and builds a semantic search query.
- `utils/format.py` - structured schema for hiring requirement extraction.
- `app.py` - FastAPI wrapper with `/health` and `/chat` endpoints.
- `tools.py` - defines the `search_tool` used by the agent to query the vector store.

## Requirements

- Python 3.13+
- `poppler` is not required for this repo; dependencies are in `pyproject.toml`.

## Install

```powershell
cd "c:\Users\HARDIK\Desktop\Hardik\Projects\Salesforce task"
python -m pip install -r requirements.txt
```

If you prefer using the project metadata:

```powershell
python -m pip install .
```

## Setup

1. Create a `.env` file if you need environment-specific variables.
2. Ensure the `catalog.json` file is present in the project root.
3. The vector store is created in `./vector_store` during runtime.

## Running the app

Start the FastAPI app with Uvicorn:

```powershell
uv run uvicorn app:app --reload
```

Then:

- `GET /health` returns service status.
- `POST /chat` accepts JSON payload matching `ChatRequest` and returns a recommended assessment response.

Example request body:

```json
{
  "messages": [
    {"role": "user", "content": "We need a leadership assessment for a senior executive."}
  ]
}
```

## How it works

1. `main.py` calls `build_docs()` and `build_vector_store()`.
2. The catalog is converted into documents and stored as embeddings via SentenceTransformers and Chroma.
3. `extract_hiring_requirements()` parses the conversation into structured hiring data.
4. `build_query()` converts the extracted data into a semantic search query.
5. The agent uses `search_tool` to find catalog matches and returns recommendations.

## Notes

- The current agent is configured to work with SHL assessment catalog data only.
- `search_tool` currently returns metadata from the Chroma collection.
- The system prompt in `agent.py` strongly constrains the agent to avoid hallucinations and recommend only catalog items.

## Project structure

- `agent.py` - agent creation and system prompt
- `app.py` - API endpoints
- `catalog.json` - SHL catalog data source
- `docs_builder.py` - converts catalog items to documents
- `main.py` - orchestration entry point
- `models.py` - Pydantic request models
- `tools.py` - search tool implementation
- `Vector_store.py` - vector store builder
- `utils/` - helper extraction and formatting logic

## Future improvements

- Add persistence for model outputs and tool search logs.
- Expand catalog metadata in the vector store.
- Add unit tests for extraction, query generation, and agent tool flow.
- Improve error handling around missing collection or empty search results.
