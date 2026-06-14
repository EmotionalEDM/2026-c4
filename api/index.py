"""Vercel serverless entrypoint — exposes the full FastAPI backend as ASGI.

All requests are rewritten to this handler by vercel.json.
Vercel Python runtime natively detects and serves ASGI applications.
"""
import sys
from pathlib import Path

# Ensure the project root is on sys.path so 'backend.app' imports resolve
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from backend.app.main import app
