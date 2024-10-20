from fastapi import FastAPI
from .Mongo import fetch

## FastAPI Config ---------------------------------
app = FastAPI()
   
## Route Config ----------------------------------- 
@app.get("/")
async def index():
    message = fetch()
    return message