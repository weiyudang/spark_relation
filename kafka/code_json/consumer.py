from kafka import KafkaConsumer
import json
import msgpack

consumer = KafkaConsumer( bootstrap_servers= ['localhost:9092'],
                          value_deserializer=msgpack.loads
                          # value_deserializer=lambda m: json.loads(m.decode('ascii'))
                          )
consumer.subscribe(topics= ['model'])
for msg in consumer:
    print(msg.value)