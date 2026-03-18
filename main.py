import random
from fastmcp import FastMCP

# create server instance
mcp = FastMCP(name="Demo Server")

@mcp.tool
def subtract(a: float, b: float)->float:
    ''' subtract two Numbers'''
    return a - b

@mcp.tool
def multiply(a: float, b: float)->float:
    ''' multiply two Numbers'''
    return a * b

@mcp.tool
def devide(a: float, b: float)->float:
    ''' devide two Numbers'''
    return a / b    

@mcp.tool
def my_tool():
    ''' Give the info about the server '''
    return "Hello, I am Virat Kohli . This is server which is using for mini calc"

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)


# install uv -> pip install uv
# uv init
# uv add fastmcp
# uv run fastmcp version
# uv run fastmcp dev inspector main.py
# uv run fastmcp run main.py
# uv run fastmcp install claude-desktop main.py
