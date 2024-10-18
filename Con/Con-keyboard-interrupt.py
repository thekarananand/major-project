import time
time.sleep(3)
##-----------------------------------------------------
import RabbitMQ, sys, logging, json

RabbitMQ.channel.queue_declare(queue='MQ')
logging.basicConfig(format='%(message)s')
##-----------------------------------------------------
def callback(ch, method, properties, body):
    message = json.loads(body)
    logging.warning(f" [x] Received {message}")
##-----------------------------------------------------
def main():
    RabbitMQ.channel.basic_consume(
        queue='MQ',
        on_message_callback=callback,
        auto_ack=True
    )

    logging.warning(' [*] Consumer Ready! Waiting for messages....')
    RabbitMQ.channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)