from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello/")
async def hello():
    ret = """<html><body><h2>Hello World!</h2></body></html>"""
    return HTMLResponse(content=ret)

if __name__ == "__main__":
    uvicorn.run("html_rs:app", host="127.111.0.0", port=5555, reload=True)
# http://127.111.0.0:5555/hello/