import requests
from config import Config
from fastmcp import FastMCP
from db import init_db
from contextlib import asynccontextmanager




@asynccontextmanager
async def life_span(mcp:FastMCP):
    print("starting up")
    await init_db()
    yield
    print("stopped")

mcp = FastMCP(name="Toggle assistance", lifespan = life_span)




@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""

    return a * b


email = Config.userEmail
password = Config.userPassword

@mcp.tool
def login():
    res  = requests.post("https://accounts.toggl.com/api/sessions",json = {"email":email,"password":password})


    print(res.json())
    return res.text
















if __name__ == "__main__":
    mcp.run()
