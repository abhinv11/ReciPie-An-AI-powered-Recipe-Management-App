from fastapi import APIRouter
from models.models import Recipe
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from config.db import conn
from fastapi.templating import Jinja2Templates
from schemas.schemas import RecipeEntity, RecipesEntity
import os

recipe = APIRouter()

# Get absolute path for templates
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(base_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)

db = conn["ReciPie"]
collection = db["recipie"]

@recipe.get("/", response_class=HTMLResponse)
async def read_item(request: Request, search: str = None):
    
    # Build search query
    query = {}
    if search:
        # Search in name, ingredients, and method fields
        query = {
            "$or": [
                {"name": {"$regex": search, "$options": "i"}},
                {"ingredients": {"$regex": search, "$options": "i"}},
                {"method": {"$regex": search, "$options": "i"}}
            ]
        }
    
    docs = collection.find(query)
    newDocs = []

    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "name": doc.get("name", ""),
            "ingredients": doc.get("ingredients", []),
            "method": doc.get("method", "")
        })

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "newDocs": newDocs, "search_query": search}
    )

@recipe.post("/")
async  def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)

    recipe = collection.insert_one(formDict)
    return {"Success": True}



@recipe.get("/edit/{id}")
async def edit_recipe(request: Request, id: str):
    from bson import ObjectId
    
    doc = collection.find_one({"_id": ObjectId(id)})
    if not doc:
        return RedirectResponse(url="/", status_code=303)
    
    recipe_data = {
        "id": str(doc["_id"]),
        "name": doc.get("name", ""),
        "ingredients": doc.get("ingredients", []),
        "method": doc.get("method", "")
    }
    
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "recipe": recipe_data}
    )

@recipe.post("/update/{id}")
async def update_recipe_form(request: Request, id: str):
    from bson import ObjectId
    from fastapi.responses import RedirectResponse
    
    form = await request.form()
    formDict = dict(form)
    
    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": formDict}
    )
    return RedirectResponse(url="/", status_code=303)

@recipe.get("/delete/{id}")
async def delete_recipe(id: str):
    from bson import ObjectId
    from fastapi.responses import RedirectResponse
    
    collection.delete_one({"_id": ObjectId(id)})
    return RedirectResponse(url="/", status_code=303)

# AI Chat Routes
from pydantic import BaseModel
import sys
sys.path.append("..")
from chatbot import get_recipe_response, clear_history

class ChatMessage(BaseModel):
    message: str

@recipe.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@recipe.post("/chat/message")
async def chat_message(chat_msg: ChatMessage):
    try:
        response = get_recipe_response(chat_msg.message)
        return {"response": response}
    except Exception as e:
        return {"response": f"Sorry, I encountered an error: {str(e)}"}

@recipe.post("/chat/clear")
async def clear_chat_history():
    clear_history()
    return {"status": "success"}