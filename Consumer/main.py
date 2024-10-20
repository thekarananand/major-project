import logging, json
from RabbitMQ import RabbitMQ
import Mongo

## RabbitMQ Config --------------------------------    
RabbitMQ.queue_declare(queue='IngressData')
logging.basicConfig(format='%(message)s')

## Call Back Function -----------------------------
def callback_function(ch, method, properties, body):
    message = json.loads(body)
    Mongo.save(message)
    logging.warning(f" [x] Received {message}")

## Driver Code ------------------------------------
RabbitMQ.basic_consume(
    queue='IngressData',
    on_message_callback=callback_function,
    auto_ack=True
)

logging.warning(' [*] Consumer Ready! Waiting for messages....')
RabbitMQ.start_consuming()