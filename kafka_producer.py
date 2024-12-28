
import os
import time 
import json 
import random 
from datetime import datetime
#from data_generator import generate_message
from book_data_generator import generate_message2
from kafka import KafkaProducer

os.chdir('C:\\test')

print('Iniciando producer')

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)


if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = generate_message2()
        
        # Send it to our 'messages' topic
        print(f'Producing message: {datetime.now()} | Message = {str(dummy_message)}')
        topic = 'messages'
        producer.send(topic, dummy_message)
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 3)
        time.sleep(time_to_sleep)
