from pyspark.sql import SparkSession
import pandas as pd

# make spark session
def make_spark_session():
    spark = SparkSession.builder.getOrCreate()
    return spark

# load .env variable 
def load_env(): 
  conf = {}
  with open('.env', 'r') as f:
    for line in f:
      key, value = line.strip().split('=')
      conf[key] = value
  return conf

# news 테이블에서 일별로 읽어서 반환
def mysql_read_day(year_month_day):
    conf = load_env()
    news = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", f"jdbc:mysql://{conf['HOST']}:{conf['PORT']}/{conf['DB']}") \
    .option("dbtable", f"(SELECT * FROM news WHERE DATE_FORMAT(datetime, '%Y-%m-%d') = '{year_month_day}') AS subquery") \
    .option("numPartitions", 5) \
    .option("user", f"{conf['USER']}") \
    .option("password", f"{conf['PWD']}") \
    .load()
    return news

# day_news란 데이터프레임을 받아서 파일명은 day_str.parquet형식으로 저장
def parquet_hadoop_input(day_news,day_str):
    conf = load_env()
    hdfs_path = f"hdfs://{conf['HADOOP_HOST']}:8020/news_data/{day_str}.parquet"
    day_news.write.parquet(hdfs_path)


def main():
    # 2024-05-02일부터 2024-07-07 끼리 일별로 mysql에 읽어서 hadoop 저장
    for day in pd.date_range(start='2024-05-02', end='2024-07-07'):
        day_str = day.strftime('%Y-%m-%d')
        # print(day_str)
        day_news = mysql_read_day(day_str)
        parquet_hadoop_input(day_news,day_str)


if __name__ == '__main__':
  main()

