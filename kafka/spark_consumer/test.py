from pyspark.sql import SparkSession
# test spark

if __name__ == '__main__':

    sqlContext = SparkSession.builder.master('local').enableHiveSupport().getOrCreate()
    sqlContext.sql("show databases").show()
