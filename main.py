from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the Item you would like to view")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = Query(None, title= "Name", description = "Name of item.")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}      

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]    