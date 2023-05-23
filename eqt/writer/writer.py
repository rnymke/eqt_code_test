# import pyspark

def write_local(df, path):
    df.to_json(path, orient="records")

def write_hive(spark, df, target):
    ### If this is the main functionality, it should just be a spark package from the getgo
    #schema = get_spark_schema()
    #df_spark = spark.createDataFrame(df, schema)
    #spark.write.saveAsTable(target) | spark.write.parquet(path)
    pass

def write_bigquery():
    pass

# ...