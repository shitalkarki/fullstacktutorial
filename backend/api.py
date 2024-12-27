from fastapi import FastAPI
from fastapi.responses import FileResponse
# Create a FastAPI app instance
app = FastAPI()

# Define a route that returns a string
@app.get("/facebook/profile")
def profile():
    return "profile"

@app.get("/facebook/chat")
def chat():
    return "chat"

@app.get("/add")
def add(a:int,b:int):
    return a+b

@app.get("/getName")
def add(a:str,b:str):
    return a+" "+b

@app.get("/getImage")
def image():
    path="song.mp3"
    return FileResponse(path, media_type="audio/mpeg", headers={"Content-Disposition": "inline; filename=song.mp3"})




