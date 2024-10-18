import time
time.sleep(4)
##-----------------------------------------------------
import RabbitMQ, sys, logging, json

RabbitMQ.channel.queue_declare(queue='MQ')
logging.basicConfig(format='%(message)s')
##-----------------------------------------------------

def callback_function(ch, method, properties, body):
    message = json.loads(body)
    logging.warning(f" [x] Received {message}")

##-----------------------------------------------------

RabbitMQ.channel.basic_consume(
    queue='MQ',
    on_message_callback=callback_function,
    auto_ack=True
)
logging.warning(' [*] Consumer Ready! Waiting for messages....')
RabbitMQ.channel.start_consuming()