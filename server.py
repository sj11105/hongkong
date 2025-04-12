from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()  # like creating an Express app or Go HTTP server

# Request/response schema using Pydantic
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Health check route
@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

# Get item by ID (dummy)
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item"}

# Create item (POST request)
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
