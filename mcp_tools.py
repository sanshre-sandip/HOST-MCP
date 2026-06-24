from fastmcp import FastMCP
from database import session
from database_models import Order

mcp = FastMCP("Order MCP System")

@mcp.tool()
def create_order(product: str, quantity: int, price: float):
    db = session()
    try:
        order = Order(product=product, quantity=quantity, price=price)
        db.add(order)
        db.commit()
        db.refresh(order)
        return {"order_id": order.id}
    finally:
        db.close()

@mcp.tool()
def list_orders():
    db = session()
    try:
        orders = db.query(Order).all()
        return [
            {"id": o.id, "product": o.product, "quantity": o.quantity, "price": o.price}
            for o in orders
        ]
    finally:
        db.close()

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8765
    )