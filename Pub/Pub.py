import time
time.sleep(6)
##-----------------------------------------------------
import RabbitMQ, logging, json

RabbitMQ.channel.queue_declare(queue='MQ')
logging.basicConfig(format='%(message)s')
##-----------------------------------------------------

for i in range(10):
    message = {
        "id"   : i,
        "text" : "Hello World"
    }
    
    RabbitMQ.channel.basic_publish(
        exchange='',
        routing_key='MQ',
        body=json.dumps(message)
    )
    logging.warning(f" [x] Sent {message}")

RabbitMQ.connection.close()