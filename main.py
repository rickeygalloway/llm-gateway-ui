import os
from contextlib import asynccontextmanager

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()

GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8080")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.client = httpx.AsyncClient(timeout=120.0)
    yield
    await app.state.client.aclose()


app = FastAPI(lifespan=lifespan)


@app.get("/api/health")
async def health(request: Request):
    try:
        resp = await request.app.state.client.get(f"{GATEWAY_URL}/healthz")
        return JSONResponse(content=resp.json(), status_code=resp.status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=503)


@app.get("/api/ready")
async def ready(request: Request):
    try:
        resp = await request.app.state.client.get(f"{GATEWAY_URL}/readyz")
        return JSONResponse(content=resp.json(), status_code=resp.status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=503)


@app.get("/api/models")
async def models(request: Request):
    try:
        resp = await request.app.state.client.get(f"{GATEWAY_URL}/v1/models")
        return JSONResponse(content=resp.json(), status_code=resp.status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=503)


@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    streaming = body.get("stream", False)

    if not streaming:
        try:
            resp = await request.app.state.client.post(
                f"{GATEWAY_URL}/v1/chat/completions",
                json=body,
            )
            return JSONResponse(content=resp.json(), status_code=resp.status_code)
        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=503)

    async def stream_gen():
        try:
            async with request.app.state.client.stream(
                "POST",
                f"{GATEWAY_URL}/v1/chat/completions",
                json=body,
            ) as resp:
                async for chunk in resp.aiter_bytes():
                    yield chunk
        except Exception as e:
            yield f"data: {{'error': '{e}'}}\n\n".encode()

    return StreamingResponse(stream_gen(), media_type="text/event-stream")


app.mount("/", StaticFiles(directory="static", html=True), name="static")
