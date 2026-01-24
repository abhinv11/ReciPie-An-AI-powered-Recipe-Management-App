def RecipeEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "ingredients": item["ingredients"],
        "method": item["method"]
    }

def RecipesEntity(items) -> list:
    return [RecipeEntity(item) for item in items]