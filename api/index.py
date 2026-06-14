"""Vercel serverless entrypoint — wraps the full FastAPI backend with Mangum.

All /api/* requests are rewritten to this handler by vercel.json.
"""
import sys
from pathlib import Path

# Ensure the project root is on sys.path so 'backend.app' imports resolve
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from mangum import Mangum
from backend.app.main import app

handler = Mangum(app)
