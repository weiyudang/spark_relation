# coding:utf-8
from kafka import KafkaConsumer
from kafka import TopicPartition
# kafka-topics --list --zookeeper localhost:2181
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], consumer_timeout_ms=10000)
# 订阅接受多个topic小心
consumer.subscribe(topics=['model','sunday'])
print(consumer.topics())
# 手动分配分区
# consumer.assign([TopicPartition(topic="model", partition=0)])
for msg in consumer:
    msg_str = msg.value
    print(msg_str.decode("utf-8"))


