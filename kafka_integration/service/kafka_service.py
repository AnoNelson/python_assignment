import json

from confluent_kafka import Producer, Consumer
from django.conf import settings


class KafkaService:
    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': settings.KAFKA_BROKER_URL,
            'enable.idempotence': True,  # Enable idempotence
            'acks': 'all',  # Wait for acknowledgments from all replicas
            'retries': 5,
        })

        self.consumer = Consumer({
            'bootstrap.servers': settings.KAFKA_BROKER_URL,
            'group.id': 'hospitalmanagement',
            'auto.offset.reset': 'earliest',
        })

    def produce_message(self, topic, message):
        # Serialize the dictionary to a JSON string
        serialized_message = json.dumps(message).encode('utf-8')
        self.producer.produce(topic, serialized_message)
        self.producer.flush()

    def consume_messages(self):
        self.consumer.subscribe([settings.KAFKA_TOPIC])

        while True:
            msg = self.consumer.poll(1.0)  # Timeout in seconds
            if msg is None:
                continue
            if msg.error():
                print(f"Error: {msg.error()}")
                continue
            print(f"Received message: {msg.value().decode('utf-8')}")
