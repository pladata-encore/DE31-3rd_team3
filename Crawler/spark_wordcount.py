from pyspark.sql import SparkSession
import pandas as pd
import MeCab
from tqdm import tqdm


# spark create
def spark_session_create():
    spark = SparkSession.builder.getOrCreate()
    return spark

 # .env 변수
def road_env(): 
    conf = {}
    with open('/home/hadoop/DE31-3rd_team3/.env', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            conf[key] = value
    return conf   

# token화 시키기
def word_tokenize(line):
    try:
        mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic')
        result = mecab.parse(line)
        return result.strip()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# 딕셔너리에 저장
def n_into_dict(answer_dic,token_out):
    lines = token_out.strip().split('\n')
    for i in lines:
        try:
            word= i.split("\t")[0]
            stop_check = i.split("\t")[1].split(",")[0]
            if stop_check[0] =="N":
                if word not in answer_dic:
                    answer_dic[word]=1
                else:
                    answer_dic[word]+=1
        except IndexError:
            continue
    return answer_dic

# read_hadoop_data_filename_list
def read_hadoop_data_filename_list():
    news_day_file_name_list = !hadoop fs -ls /news_data
    news_day_file_name_list = news_day_file_name_list[1:] #첫값은 쓸데없는거라서
    return news_day_file_name_list

# filename_token
def filename_token(news_day_file_name_list):
    news_day_file_name_split_list = []
    for i in range(len(news_day_file_name_list)):
        news_day_file_name_split_list.append(news_day_file_name_list[i].split("news_data/")[1])
    return news_day_file_name_split_list

# make dict()
def parquet_read(spark, filename_token(read_hadoop_data_filename_list)):
    answer_dic = {} #최종 딕셔너리
    for i in tqdm(range(len(filename_token(read_hadoop_data_filename_list)))): #전체 파일 리스트개수만킄
        df = spark.read.parquet(f"hdfs://{conf['HADOOP_HOST']}:{conf['HADOOP_PORT']}/news_data/{filename_token(read_hadoop_data_filename_list)[i]}") 
        small_dict(answer_dic,df)
    return answer_dic

# small dict()    
def small_dict(answer_dic,df):
    for j in range(1,df.count()+1):  # df.count()는 DataFrame의 전체 행 수입니다
        filtered_row = df.filter(df['id'] == j).select('content').first()  # 첫 번째 행 가져오기
        filtered_content = filtered_row['content']  # 'content' 열의 값을 가져옴
        output = word_tokenize(filtered_content)
        n_into_dict(answer_dic, output)
        return answer_dic

# main
def main():
    spark = spark_session_create()
    answer_dict = parquet_read(spark, filename_token(read_hadoop_data_filename_list))

if __name__ == '__main__':
  main()