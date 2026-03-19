# llm-gateway-ui

## Project Type

Python

## Commands

- **Format**: `ruff format .`
- **Lint**: `ruff check .`
- **Type check**: `mypy .`
- **Install deps**: `pip install -r requirements.txt`

## Conventions

- Python 3.11+
- Line length: 100
- Use `.venv/` for virtual environment
- Pre-commit hooks run ruff lint, ruff format, gitleaks on commit
- Never commit `.env` — use `.env.example` as template
- Config via environment variables loaded from `.env`
- `from __future__ import annotations` at the top of every module
- Proxy pattern: all routes in `main.py` forward to `GATEWAY_URL` via `httpx.AsyncClient`
- Streaming responses use SSE — preserve `text/event-stream` content-type pass-through
