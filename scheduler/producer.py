import os
import pika

def produce(host, body):
    # declare the RabbitMQ connection parameters
    rabbitmq_url = os.environ.get("RABBITMQ_URI", "amqp://admin:rabbitmq@rabbitmq:5672/")

    parameters = pika.URLParameters(rabbitmq_url)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # declare the exchange and queue, and bind them together
    channel.exchange_declare(exchange="jobs", exchange_type="direct")
    channel.queue_declare(queue="router_jobs")
    channel.queue_bind(queue="router_jobs", exchange="jobs", routing_key="check_interfaces")

    # publish the messagew
    channel.basic_publish(exchange="jobs", routing_key="check_interfaces", body=body)

    connection.close()

if __name__=='__main__':
    produce("localhost", "192.168.1.10")