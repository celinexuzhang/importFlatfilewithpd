import pyspark
#Import SparkSession from pyspark.sql.
#Make a new SparkSession called my_spark using SparkSession.builder.getOrCreate().
#Print my_spark to the console to verify it's a SparkSession.

from pyspark.sql import SparkSession
# Create my_spark
my_spark = SparkSession.builder.getOrCreate()
df = spark.read.json('C:/Users/celin/Downloads/Python-and-Spark-for-Big-Data-master/Python-and-Spark-for-Big-Data-master/Spark_DataFrames/people.jason')
df.show()


