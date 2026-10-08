from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Items REST API",
    description="REST API for managing items",
    version="1.0.0"
)


class Item(BaseModel):
    name: str
    description: str
    price: float


items = {}
next_id = 1


@app.get("/api/items")
def get_items():
    return list(items.values())


@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return items[item_id]


@app.post("/api/items", status_code=201)
def create_item(item: Item):
    global next_id

    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
        "price": item.price
    }

    items[next_id] = new_item
    next_id += 1

    return new_item


@app.put("/api/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = {
        "id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price
    }

    items[item_id] = updated_item

    return updated_item


@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    deleted_item = items.pop(item_id)

    return {
        "message": "Item deleted",
        "item": deleted_item
    }