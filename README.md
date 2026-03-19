# LLM Gateway UI

A Python FastAPI web app that wraps and demonstrates every feature of [go-llm-gateway](../go-llm-gateway). Provides a ChatGPT-style chat interface with streaming, provider health monitoring, and full model control.

## Prerequisites

- Python 3.9+
- [go-llm-gateway](../go-llm-gateway) running on `http://localhost:8080`

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` if your gateway runs on a different address.

## Run

```bash
uvicorn main:app --reload --port 3000
```

Open [http://localhost:3000](http://localhost:3000).

## Features

| Feature | Description |
|---|---|
| Model selector | Populates from `/v1/models`, grouped by provider |
| Non-streaming chat | Full response returned at once |
| Streaming chat | SSE tokens rendered in real time with blinking cursor |
| Stop generation | Abort button cancels in-flight stream |
| System prompt | Prepended as `{"role": "system"}` to every request |
| Temperature / max tokens | Sliders wired to request body |
| Provider health panel | Polls `/readyz` every 10s, colored dot per provider |
| Gateway liveness | Polls `/healthz`, shows connected/disconnected |
| Markdown rendering | Code blocks and inline code via marked.js CDN |
| Token usage | Shows prompt / completion / total after non-streaming responses |
| Copy message | One-click copy on each assistant bubble |
| New conversation | Clears message history |

## API Endpoints

| UI feature | Python endpoint | Gateway endpoint |
|---|---|---|
| Model dropdown | `GET /api/models` | `GET /v1/models` |
| Chat | `POST /api/chat` | `POST /v1/chat/completions` |
| Streaming | `POST /api/chat` (stream: true) | SSE from `/v1/chat/completions` |
| Health badge | `GET /api/health` | `GET /healthz` |
| Provider status | `GET /api/ready` | `GET /readyz` |

## Configuration

| Variable | Default | Description |
|---|---|---|
| `GATEWAY_URL` | `http://localhost:8080` | go-llm-gateway base URL |
| `HOST` | `0.0.0.0` | Bind address (used when running directly) |
| `PORT` | `3000` | Port (used when running directly) |
