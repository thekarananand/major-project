from RabbitMQ import RabbitMQ
import logging, json
import numpy as np

## RabbitMQ Config --------------------------------    
RabbitMQ.queue_declare(queue='IngressData')
logging.basicConfig(format='%(message)s')

## Route Config ----------------------------------- 

x = 0;

while (True):
    y = np.sin(x) 
    x += 0.05
    
    message = {
        "PV1": round(x,2),
        "PV2": y
    }
        
    RabbitMQ.basic_publish(
        exchange='',
        routing_key='IngressData',
        body=json.dumps(message)
    )
        
    logging.warning(f" [x] Pushed {message}")