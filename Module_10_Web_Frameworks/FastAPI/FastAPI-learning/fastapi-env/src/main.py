from typing import Union

from fastapi import FastAPI

app = FastAPI()

# Run the server with: uvicorn src.main:app

# Check it: Open your browser at http://127.0.0.1:8000/items/5?q=somequery

# Interactive API docs: go to http://127.0.0.1:8000/docs

# Alternative API docs: go to http://127.0.0.1:8000/redoc

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}