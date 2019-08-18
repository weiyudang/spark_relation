# coding:utf-8
from kafka import KafkaProducer
import time
from faker import Faker
# kafka-console-producer  --broker-list localhost:9092 --topic model
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
i = 0
fake = Faker()
for _ in range(2):
    print fake.text()
while True:
    time_str = time.strftime(time.ctime())
    send_str = "这是第{}条信息{}".format(i, time_str)
    future = producer.send('model', key=b'Time', value= str(fake.text()), partition=0)
    result = future.get(timeout=10)
    i += 1
    time.sleep(1)

    # print(result)/
