from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import uvicorn
import os

# Create FastAPI instance
app = FastAPI()

# Ensure correct relative path for templates
base_dir = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))

# Define route for rendering HTML
@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("jira_operation.html", {"request": request})

# Run the FastAPI application
if __name__ == "__main__":
    uvicorn.run("template_rs:app", host="127.111.0.0", port=5555, reload=True)
