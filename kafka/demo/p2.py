# coding:utf-8
from kafka import KafkaProducer
import time

# kafka-console-producer  --broker-list localhost:9092 --topic model
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
i = 0
while True:
    time_str = time.strftime(time.ctime())
    send_str = "这是第{}条信息{} from {}".format(i, time_str, "sunday")
    future = producer.send('model', key=b'Time', value=send_str, partition=0)
    result = future.get(timeout=10)
    i += 1
    time.sleep(2)
