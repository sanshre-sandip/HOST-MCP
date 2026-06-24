from fastmcp import FastMCP
from database import session, engine
import database_models

database_models.Base.metadata.create_all(bind=engine)

db = session()
mcp = FastMCP("My Server")

@mcp.tool
def process_data(input: str) -> str:
    """Process data on the server"""
    return f"Processed: {input}"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)