import sys

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def echo(rdd):
    print rdd


if __name__ == '__main__':
    sc = SparkContext(appName="text")
    ssc = StreamingContext(sc, 5)
    broker = "localhost:2181"
    topic = "model"
    kbrokers = "localhost:9092"
    # kvs=KafkaUtils.createStream(ssc,broker,"3e",{topic:1},kafkaParams={"metadata.broker.list":kbrokers})
    # kvs = KafkaUtils.createStream(ssc, "localhost:2181", 'spark', {"model": 1})
    kvs=KafkaUtils.createDirectStream(ssc,["model"],{"metadata.broker.list": kbrokers})
    lines = kvs.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
    counts.pprint()

    ssc.start()

    ssc.awaitTermination()
