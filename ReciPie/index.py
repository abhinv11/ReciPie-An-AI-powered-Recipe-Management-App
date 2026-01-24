from fastapi import FastAPI
from routes.routes import recipe
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount static files only if directory exists (for local dev)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(recipe)

# For Vercel
handler = app