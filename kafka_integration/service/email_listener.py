import json
import sys
import threading
from confluent_kafka import Consumer
from confluent_kafka import KafkaError
from confluent_kafka import KafkaException
from django.core.mail import send_mail

from hospitalmanagement import settings

# We want to run thread in an infinite loop
running = True
conf = {'bootstrap.servers': settings.KAFKA_BROKER_URL,
        'auto.offset.reset': 'smallest',
        'group.id': "user_group"}
# Topic
topic = settings.KAFKA_TOPIC


class UserCreatedListener(threading.Thread):
    def __init__(self):
        print("creating object")
        threading.Thread.__init__(self)
        # Create consumer
        self.consumer = Consumer(conf)

    def run(self):
        print('Inside EmailService :  Created Listener ')
        try:
            # Subscribe to topic
            self.consumer.subscribe([topic])
            while running:
                # Poll for message
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue
                # Handle Error
                if msg.error():
                    if msg.error().code() == KafkaError.PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                         (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
                else:
                    # Handle Message
                    print('---------> Got message Sending email.....')
                    message = json.loads(msg.value().decode('utf-8'))
                    name = message.get('name')
                    email = message.get('email')
                    message_ = message.get('message')

                    send_mail('Contact Form submission of:' + str(name) + ' || ' + str(email), message_, settings.EMAIL_HOST_USER,
                              settings.EMAIL_RECEIVING_USER, fail_silently=False)

                    # In Real world, write email sending logic here
                    print(message.get("email"))
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()
