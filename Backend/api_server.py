# import libs for FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# import libs for uvicorn
import uvicorn

# import libs for sql query
from sqlalchemy import create_engine, text

# import libs for datetime
from datetime import datetime, timedelta

# import libs for make wordtreemap
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import squarify
import io

# add font family for squarify
fontpath = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = fm.FontProperties(fname=fontpath, size=10).get_name() 
plt.rc('font', family=font_name)

app = FastAPI()

# Enable CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# load db engine
def _make_engine():
  # read environment variables from .env file
  conf = {}
  with open('../.env', 'r') as f:
    for line in f:
      key, value = line.strip().split('=')
      conf[key] = value

  # connect to mysql
  engine = create_engine('mysql+pymysql://'+conf['USER']+':'+conf['PWD']+'@'+conf['HOST']+':'+conf['PORT']+'/'+conf['DB'])
  return engine

engine = _make_engine()

def _excute_sql(sql):
  with engine.connect() as con: # Connect
    stmt = text(sql)  # Convert the SQL STateMenT to an executable object
    print(stmt) # debug
    rs = con.execute(stmt) 
    keys = rs.keys()
    data = [dict(zip(keys, row)) for row in rs] # parse result as dict
    con.close() # Close the connection
    return data

def _get_word_count(startdate, enddate, main_sec, sub_sub, limit=500):
  st_datetime = datetime.strptime(startdate, "%Y-%m-%d")
  ed_datetime = datetime.strptime(enddate, "%Y-%m-%d") + timedelta(days=1) - timedelta(seconds=1)
  sql = f"SELECT word AS 'name', SUM(frequency) AS value FROM word_counts WHERE datetime BETWEEN '{st_datetime}' AND '{ed_datetime}' GROUP BY word ORDER BY value DESC LIMIT {limit}"
  # sql = f"SELECT datetime, word, frequency FROM word_counts WHERE datetime BETWEEN '{st_datetime}' AND '{ed_datetime}' AND main_sec = '{main_sec}' AND sub_sub = '{sub_sub}' ORDER BY frequency DESC LIMIT {limit}"
  data = _excute_sql(sql)
  return data

def _make_word_treemap_to_img(data):
  # make word treemap
  # decimal.Decimal to int
  data_size = [int(d['value']) for d in data]
  data_label = [d['key'] for d in data]
  print(data_size, data_label)
  plt.figure(figsize=(10, 10))
  # set font for squarify
  squarify.plot(sizes=data_size, label=data_label, alpha=0.7)
  plt.axis('off')
  
  # save word treemap as image in buffer
  img_buffer = io.BytesIO()
  plt.savefig(img_buffer, format='png')
  img_buffer.seek(0)
  return img_buffer

################################### debug ###################################
@app.get("/api/v1/health") # health check
def health():
  return {"status": "ok"}
#############################################################################


#################################### API ####################################
@app.get("/api/v1/sql") # sql query
def sql():
  sql = "SELECT * FROM news LIMIT 10"

  data = _excute_sql(sql)
  return {"data": data}

@app.get("/api/v1/news_betwn_range") # get news info at selected date
def rangenews(start_date: str, end_date: str):
  # start_date = "2024-05-01"
  # end_date = "2024-05-01"
  data = _get_word_count(start_date, end_date, '100', '269')
  print(len(data))
  # img_buffer = _make_word_treemap_to_img(data)
  return {"data": data}

@app.get("/api/v1/search_news") # search news info by keyword
def searchnews(keyword: str, date: str):
  # keyword = "정부"
  # date = "2024-05-04"
  # get wordcount from -3 ~ +3 days
  st_datetime = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=3)
  ed_datetime = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=4)
  # group by datetime and word
  sql = f"SELECT datetime, word, SUM(frequency) as frequency FROM word_counts WHERE datetime BETWEEN '{st_datetime}' AND '{ed_datetime}' AND word = '{keyword}' GROUP BY datetime, word ORDER BY datetime"

  data = _excute_sql(sql)
  return {"data": data}
#############################################################################


# run the server
if __name__ == "__main__":
  # autoreload=True for debug
  uvicorn.run("api_server:app", host="0.0.0.0", port=21080, reload=True)
