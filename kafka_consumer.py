#https://www.w3schools.com/python/python_mongodb_insert.asp

import os
import json
from kafka import KafkaConsumer
from pymongo import MongoClient

os.chdir('C:\\test')

client = MongoClient('localhost', 27017)
#client.server_info()
db = client.db_test

print('Iniciando consumer')

if __name__ == '__main__':
    #kafka consumer
    topic = 'messages'
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    for message in consumer:
        print(json.loads(message.value))
        lst = json.loads(message.value)
        db = client.db_test
        collection = db['test_collection']
        print(collection)
        #response = collection.insert_one(json.loads(message.value)) #insert_many w/ value is list
        response = collection.insert_many(lst) #insert_many    raise TypeError("documents must be a non-empty list") TypeError: documents must be a non-empty list
        #print('Registro incluido com sucesso. Id: ' + str(response.inserted_id))
        #print('Total de registros inseridos: ', len(response.inserted_ids))
        #print('Registro incluido com sucesso. Id: ' + str(response.inserted_ids)) #inserted_ids many
