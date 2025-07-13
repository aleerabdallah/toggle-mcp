#import asyncio
#from fastmcp import Client


from mcp_server.main import mcp
import sys
# In-memory server (ideal for testing)
## server = FastMCP("TestServer")
# client = Client(server)

# HTTP server
# client = Client("https://example.com/mcp")

# Local Python script




def main():
    try:
        mcp.run()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
