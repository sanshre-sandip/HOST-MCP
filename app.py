from fastapi import FastAPI
from mcp_tools import create_order, list_orders

app = FastAPI(title="Order MCP Server (Hosted)")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/order")
def api_create_order(product: str, quantity: int, price: float):
    return create_order(product, quantity, price)

@app.get("/orders")
def api_list_orders():
    return list_orders()

