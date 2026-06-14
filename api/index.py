"""Vercel serverless entrypoint — diagnostic + full FastAPI backend."""
import sys
from pathlib import Path

_project_root = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, _project_root)

# Try importing the full backend; if it fails, expose the error for debugging
try:
    from backend.app.main import app as _app
    app = _app  # native ASGI — Vercel detects this automatically
except Exception as e:
    import traceback
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse

    app = FastAPI()

    @app.get("/{path:path}")
    def debug(path: str):
        return PlainTextResponse(
            f"IMPORT ERROR: {e}\n\n{traceback.format_exc()}",
            status_code=500,
        )
