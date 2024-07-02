# read csv files and save to database(mysql)
import pandas as pd
import os
import datetime
from sqlalchemy import text
from sqlalchemy import create_engine

# make date_list
date_list = [x.strftime('%Y%m%d') for x in pd.date_range(start='20240501', end='20240513')]
main_topics = [100, 101, 102, 103, 104, 105]

def _make_engine():
  # read environment variables from .env file
  conf = {}
  with open('.env', 'r') as f:
    for line in f:
      key, value = line.strip().split('=')
      conf[key] = value

  # connect to mysql
  engine = create_engine('mysql+pymysql://'+conf['USER']+':'+conf['PWD']+'@'+conf['HOST']+':'+conf['PORT']+'/'+conf['DB'])
  return engine

def _create_table(engine):
  # create table if not exists
  with engine.connect() as con:
    con.execute(text("CREATE TABLE IF NOT EXISTS news (id INT AUTO_INCREMENT PRIMARY KEY, main_section VARCHAR(50), sub_section VARCHAR(50), title TEXT, datetime datetime, content LONGTEXT, image_src TEXT, byline TEXT)"))
    
def _read_csv_files(f, curDate):
  # read csv files
  df = pd.read_csv(f)

  ################################################### preprocessing ###################################################
  # main_section,sub_section,title,datetime,content,image_src,byline

  # remove duplicates by "title", "content"
  df = df.drop_duplicates(subset=['title', 'content'])

  # estimated input format is "2024.05.09. 오후 9:34", if not replace to curDate
  # change "오전", "오후" to "AM", "PM"
  df['datetime'] = df['datetime'].apply(lambda x: x.replace('오전', 'AM').replace('오후', 'PM') if '오전' in x or '오후' in x else x)
  df['datetime'] = df['datetime'].apply(lambda x: datetime.datetime.strptime(x, '%Y.%m.%d. %p %I:%M') if '.' in x else datetime.datetime.strptime(curDate, '%Y%m%d'))
  
  #####################################################################################################################

  return df

def _save_to_database(engine, df):
  # save to database
  df.to_sql('news', con=engine, if_exists='append', index=False)

def main():
  engine = _make_engine()
  _create_table(engine)

  for date in date_list:
    full_df = pd.DataFrame()

    for topic in main_topics:
      # get data from  ./naver_news_data/{date}_news_{topic}.csv
      f = f'./naver_news_data/{date}_news_{topic}.csv'
      if not os.path.exists(f):
        continue
      df = _read_csv_files(f, date)
      full_df = pd.concat([full_df, df], ignore_index=True)
      os.remove(f)

    # save full_df as csv
    full_df.to_csv(f'./naver_news_data/{date}_news.csv', index=False)

    # save to database
    _save_to_database(engine, full_df)
    print(f"done: {date}")

if __name__ == '__main__':
  main()
