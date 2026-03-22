from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()
route_load_error = None

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "ok", "message": "ReciPie API is running"}

# Import routes after app creation
try:
    from routes.routes import recipe
    app.include_router(recipe)
except Exception as e:
    route_load_error = str(e)
    print(f"Error loading routes: {e}")

if route_load_error:
    @app.get("/")
    async def startup_error():
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Application failed to initialize routes",
                "error": route_load_error,
                "hint": "Check MONGODB_URI and GROQ_API_KEY in Vercel Environment Variables, then redeploy.",
            },
        )

# Mount static files only if directory exists
static_path = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_path):
    try:
        app.mount("/static", StaticFiles(directory=static_path), name="static")
    except Exception as e:
        print(f"Error mounting static files: {e}")

# For Vercel - this is the handler Vercel will call
app = app