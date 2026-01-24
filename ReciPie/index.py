from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "ok", "message": "ReciPie API is running"}

# Import routes after app creation
try:
    from routes.routes import recipe
    app.include_router(recipe)
except Exception as e:
    print(f"Error loading routes: {e}")

# Mount static files only if directory exists
static_path = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_path):
    try:
        app.mount("/static", StaticFiles(directory=static_path), name="static")
    except Exception as e:
        print(f"Error mounting static files: {e}")

# For Vercel - this is the handler Vercel will call
app = app