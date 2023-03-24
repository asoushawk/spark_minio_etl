def bronze_to_silver(spark) -> None:

    df = spark.read.csv('s3a://data-product-a/bronze')
    df.write.parquet('s3a://data-product-a/silver/brazilian_cities', mode='overwrite')

    #df = spark.createDataFrame([dict(a=2)])
    #df.write.csv('s3a://landing-a/data/')
    return df.count()
def silver_to_gold(spark):

    df = spark.read.parquet('s3a://data-product-a/silver/brazilian_cities')
    df.write.parquet('s3a://data-product-a/gold/brazillian', mode='overwrite')
    return df.count()