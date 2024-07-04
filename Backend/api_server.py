# import libs for FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# import libs for uvicorn
import uvicorn

# import libs for sql query
from sqlalchemy import create_engine, text

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
  with open('.env', 'r') as f:
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
def rangenews(): # def rangenews(start_date: str, end_date: str):
  start_date = "2024-05-04"
  end_date = "2024-05-04"
  sql = f"SELECT * FROM news WHERE datetime BETWEEN '{start_date}' AND '{end_date}' LIMIT 10"

  data = _excute_sql(sql)
  return {"data": data}

@app.get("/api/v1/search_news") # search news info by keyword
def searchnews(): # def searchnews(keyword: str, date: str):
  keyword = "정부"
  date = "2024-05-04"
  # get all news where date is selected date and title contains keyword
  # datetime is datetime64 type, so make sure to get every 00~23 hours news
  sql = f"SELECT  * FROM (SELECT * FROM news WHERE datetime LIKE '{date}%' AND title LIKE '%{keyword}%') AS t LIMIT 10"

  data = _excute_sql(sql)
  return {"data": data}
#############################################################################




# run the server
if __name__ == "__main__":
  # autoreload=True for debug
  uvicorn.run("api_server:app", host="0.0.0.0", port=21080, reload=True)
