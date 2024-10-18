import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='rabbitmq'
    )
)

channel = connection.channel()