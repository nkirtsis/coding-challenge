#!/usr/bin/env python
import pika, time, json

from config import input_data, rabbitmq
from process import *

process = process()
data = process.load_json_data_from_file(input_data['data_dir'] + input_data['events_file'])

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq['host']))
channel = connection.channel()

channel.queue_declare(queue=rabbitmq['queue'])

for row in data:
	print(row)
	channel.basic_publish(exchange='', routing_key=rabbitmq['queue'], body=json.dumps(row))
	time.sleep(int(rabbitmq['busy_time']))

channel.basic_publish(exchange='', routing_key=rabbitmq['queue'], body="finished")
print(" [x] Sent all messages")
connection.close()