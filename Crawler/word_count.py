from dotenv import load_dotenv
import os
import MeCab
from collections import Counter

# conf 파일 정보 불러오기
def road_env(): 
    conf = {}
    with open('./.env', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            conf[key] = value
# word_tokenize 형태소 분석하기
def word_tokenize(line):
    try:
        mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic')
        result = mecab.parse(line)
        return result.strip()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def text_file_read(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_file = file.read()  
        return text_file

def n_into_dict(token_out):
    dic = dict()
    lines = token_out.strip().split('\n')
    for i in lines:
        try:
            word= i.split("\t")[0]
            stop_check = i.split("\t")[1].split(",")[0]
            if stop_check[0] =="N":
                if word not in dic:
                    dic[word]=1
                else:
                    dic[word]+=1
        except IndexError:
            print(f"{i} ------>error") #끝에 EOS
            continue
    return dic

def main():
    road_env()
    file_path = "/home/hadoop/DE31-3rd_team3/Crawler/counter.txt"
    text_input = text_file_read(file_path)
    token_out = word_tokenize(text_input)
    dic = n_into_dict(token_out) #최종결과물
if __name__ == '__main__':
  main()