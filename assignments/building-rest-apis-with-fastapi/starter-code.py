from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Item API")


class Item(BaseModel):
    name: str
    price: float
    is_in_stock: bool = True


items = [
    {"id": 1, "name": "Laptop", "price": 999.99, "is_in_stock": True}
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}


# TODO: Add GET /items
# TODO: Add POST /items
# TODO: Add GET /items/{item_id}
# TODO: Add PUT /items/{item_id}
# TODO: Add DELETE /items/{item_id}
