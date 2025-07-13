from fastmcp import FastMCP


mcp = FastMCP(name="Toggle assistance")

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b




if __name__ == "__main__":
    mcp.run()
