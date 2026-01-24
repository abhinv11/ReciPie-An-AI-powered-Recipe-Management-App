from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    ingredients: str
    method: str