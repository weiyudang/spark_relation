# coding:utf-8
from kafka import KafkaProducer
import time
import json
import msgpack

# 若消息过大，还可压缩消息发送，可选值为 ‘gzip’, ‘snappy’, ‘lz4’, or None
producer = KafkaProducer(bootstrap_servers=["localhost:9092"],
                         value_serializer=msgpack.dumps  # 压缩传输大文件
                         # value_serializer=lambda m: json.dumps(m).encode('ascii')
                         )

while True:
    future = producer.send("model", value={"name": "weiyudang"}, partition=0)

    future.get(timeout=10)
    time.sleep(1)
