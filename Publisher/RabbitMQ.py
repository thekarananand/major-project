import pika

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='rabbitmq'
        )
    )
    
    RabbitMQ = connection.channel()
except:
    exit()