from fastapi import FastAPI
from typing import Union, Optional
import uvicorn

# Create a FastAPI instance for the server
server = FastAPI()

# Define a route for the root URL, which returns a simple welcome message
@server.get("/")
def initial():
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"Data": "Welcome Khushal!"}

# Define a route that accepts a dynamic file path, useful for serving files
@server.get("/items/{file_path:path}")
def index(file_path: str):
    """
    Endpoint that returns the requested file path.
    
    Args:
        file_path (str): The path to the file requested by the user.

    Returns:
        dict: A dictionary containing the requested file path.
    """
    return {"file_path": file_path}

# Define a route that accepts item ID and optional additional data
@server.get("/items/{item_id}")
def fun1(item_id: int, data: Union[str, None] = None):
    """
    Endpoint that returns the item ID and optionally some associated data.
    
    Args:
        item_id (int): The ID of the item.
        data (Union[str, None], optional): Optional string data related to the item. Defaults to None.

    Returns:
        dict: A dictionary with the item ID and associated data (if provided).
    """
    return {"item_id": item_id, "data": data}

# Define a route that accepts optional query parameters for product and quantity
@server.get("/items/")
def index(q: int = 0, m: Optional[int] = 10):
    """
    Endpoint that returns product and quantity, with default values for both.
    
    Args:
        q (int, optional): The product identifier. Defaults to 0.
        m (Optional[int], optional): The quantity of the product. Defaults to 10.

    Returns:
        dict: A dictionary containing the product and quantity.
    """
    return {"Prodcut is": q, "m": m}

# Print statements for debugging purposes
print("This always runs.")  # This will be printed regardless of whether the script is run directly or imported
print("--->", __name__)  # Prints the current module's name

# Run the FastAPI server if the script is executed directly
if __name__ == "__main__":
    """
    Main entry point for running the FastAPI application.
    Starts the server with hot reload on port 7777.
    """
    print("Main ....")
    uvicorn.run("fastapi_server:server", port=7777, reload=True)


# python fastapi_server.py