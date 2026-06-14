"""Vercel serverless entrypoint — wraps FastAPI with Mangum (required for Vercel serverless).

The rewrite /api/(.*) → /api/index sends all API calls here.
Mangum provides the handler() function Vercel's Python runtime expects.
"""
import sys
from pathlib import Path

_project_root = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, _project_root)

try:
    from mangum import Mangum
    from backend.app.main import app as _app
    handler = Mangum(_app, lifespan="off")
except Exception as e:
    import traceback
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse
    from mangum import Mangum

    _app = FastAPI()

    @_app.get("/{path:path}")
    def debug(path: str):
        return PlainTextResponse(
            f"IMPORT ERROR: {e}\n\n{traceback.format_exc()}",
            status_code=500,
        )

    handler = Mangum(_app, lifespan="off")
