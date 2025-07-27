import pika

from settings import URI

# params = pika.ConnectionParameters('localhost')
params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(queue="hello")

if __name__ == "__main__":

    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body="Hello, SYSDB-44! - 27.07.2025",
    )
