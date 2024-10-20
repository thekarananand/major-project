from fastapi  import FastAPI
from pydantic import BaseModel
from .RabbitMQ import RabbitMQ
import logging, json

## FastAPI Config ---------------------------------
app = FastAPI()

class DataScheme(BaseModel):
    PV1: float
    PV2: float
   
## RabbitMQ Config --------------------------------    
RabbitMQ.queue_declare(queue='IngressData')
logging.basicConfig(format='%(message)s')

## Route Config ----------------------------------- 
@app.post("/")
async def index(Body: DataScheme):
    
    message = {
        "PV1": Body.PV1,
        "PV2": Body.PV2
    }
    
    RabbitMQ.basic_publish(
        exchange='',
        routing_key='IngressData',
        body=json.dumps(message)
    )
    
    logging.warning(f" [x] Pushed {message}")
    
    return { "status" : "OK" }