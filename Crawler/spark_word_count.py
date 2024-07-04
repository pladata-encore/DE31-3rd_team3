from pyspark.sql import SparkSession
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
# import konlpy
from konlpy.tag import Mecab

########################################## Functions ##########################################
# make mysql engine
def _make_engine():
  conf = load_env()
  engine = create_engine(f"mysql+pymysql://{conf['USER']}:{conf['PWD']}@{conf['HOST']}:{conf['PORT']}/{conf['DB']}")
  return engine

# make spark session
def make_spark():
  # conf = pyspark.SparkConf().setAppName("test_khy").\
  #   setMaster("spark://192.168.0.251:5055")
  # spark = SparkSession.builder.config(conf=conf).getOrCreate()
  spark = SparkSession.builder.appName("test_khy").getOrCreate()
  spark
  return spark

# conf 파일 정보 불러오기
def load_env(): 
  conf = {}
  with open('.env', 'r') as f:
    for line in f:
      key, value = line.strip().split('=')
      conf[key] = value
  return conf

# excute sql through spark
def excute_mysql_pyspark(spark, date, main_section, sub_section):
  conf = load_env()
  # read mysql data
  jdbc_url = f"jdbc:mysql://{conf['HOST']}:{conf['PORT']}/{conf['DB']}"
  query = f"SELECT * FROM naver_miniproject.news WHERE datetime LIKE '{date}%' AND main_section = '{main_section}' AND sub_section = '{sub_section}'"
  df = spark.read.format("jdbc").option("url", jdbc_url).option("query", query).option("user", conf['USER']).option("password", conf['PWD']).load()

  return df

# save data to mysql
def to_database(engine, date, main_section, sub_section, arr):
  df = pd.DataFrame(arr.items(), columns=['word', 'frequency'])
  df['datetime'] = date
  df['main_sec'] = main_section
  df['sub_sub'] = sub_section
  df.to_sql('word_counts', con=engine, if_exists='append', index=False)

# create table
def _create_table(engine):
  with engine.connect() as con:
    query = "CREATE TABLE IF NOT EXISTS word_counts (datetime DATE, main_sec VARCHAR(20), sub_sub VARCHAR(20), word VARCHAR(50), frequency INT)"
    con.execute(text(query))


def noun_verv_tokenize(text):
  return [word for word, pos in mecab.pos(text) if pos in ['NNG', 'NNP', 'VV']]

def word_counter(counter_arr, text):
  for word in text:
    if word in counter_arr:
      counter_arr[word] += 1
    else:
      counter_arr[word] = 1
  return counter_arr
########################################## Functions ##########################################




########################################## Variables ##########################################
sections = [
            ['100','264','265','268','266','267','269'],
            ['101','259','258','261','771','260','262','310','263'],
            ['102','249','250','251','254','252','59b','255','256','276','257'],
            ['103','241','239','240','237','238','276','242','243','244','248','245'],
            ['105','731','226','227','230','732','283','229','228'],
            ['104','231','232','233','234','322'],
        ]

date_list = [x.strftime('%Y-%m-%d') for x in pd.date_range(start='20240501', end='20240520')]

mecab = Mecab()
########################################## Variables ##########################################



### Main Start ###
spark = make_spark()
engine = _make_engine()
_create_table(engine)
for date in date_list:
  for section in sections: 
    main_section = section[0]
    sub_section = section[1:]
    for sub in sub_section:
      df = excute_mysql_pyspark(spark, date, main_section, sub)
      counter_arr = {}
      for row in df.rdd.collect():
        text = row['content']
        text = noun_verv_tokenize(text)
        counter_arr = word_counter(counter_arr, text)
      to_database(engine, date, main_section, sub, counter_arr)
      print(f'{date} {main_section} {sub} done')
print('all done')    
### Main Start ###