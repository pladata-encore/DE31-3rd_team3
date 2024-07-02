import csv, time, threading, os, re
import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = [
            ['100','264','265','268','266','267','269'],
            ['101','259','258','261','771','260','262','310','263'],
            ['102','249','250','251','254','252','59b','255','256','276','257'],
            ['103','241','239','240','237','238','276','242','243','244','248','245'],
            ['105','731','226','227','230','732','283','229','228'],
            ['104','231','232','233','234','322'],
        ]

# date as YYYYMMDD between 20240501 ~ 20240630
date_list = [x.strftime('%Y%m%d') for x in pd.date_range(start='20240501', end='20240630')]

def parse_detail(res, url0, url1, curDate):
  json_data_list = []
  for i in res:
    # find href
    href = i.find('a')['href']
    req = requests.get(href)
    soup = BeautifulSoup(req.text, 'html.parser')
    # parse data-cursor
    if soup.find('div', id='ct') == None:
      continue
    else:
      div_ct = soup.find('div', id='ct')

    # find title
    if div_ct.find('h2') != None:
      title = div_ct.find('h2').text
    else:
      title = ''

    # find datetime
    if div_ct.find('span', class_='media_end_head_info_datestamp_time _ARTICLE_DATE_TIME') == None:
      datetime = curDate
    else:
      datetime = div_ct.find('span', class_='media_end_head_info_datestamp_time _ARTICLE_DATE_TIME').text

    # find content
    if div_ct.find('article', id='dic_area') == None:
      plain_text = ''
      image_src = ''
    else:
      article_dic = div_ct.find('article', id='dic_area')
      plain_text = article_dic.text.strip().replace(re.sub(r'\s+', ' ', '\n'), ' ').replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').replace('  ', ' ')
      if article_dic.find('img') == None:
        image_src = ''
      else:
        try: # try to find 'data-src' first, if not found, find 'src'
          image_src = article_dic.find('img')['data-src']
        except KeyError:
          image_src = article_dic.find('img')['src']

    # find byline
    if div_ct.find('div', class_='byline') == None:
      byline = ''
    else:
      byline = div_ct.find('div', class_='byline').text.strip().replace('\n', '')

    cur = {
      'main_section': url0,
      'sub_section': url1,
      'title': title,
      'datetime': datetime,
      'content': plain_text,
      'image_src': image_src,
      'byline': byline
    }

    # add to json_data_list
    json_data_list.append(cur)

  # write to csv (append, not overwrite)
  with open(f'{curDate}_news_{url0}_{url1}.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # check if file is empty
    if csvfile.tell() == 0:
      fieldnames = ['main_section', 'sub_section', 'title', 'datetime', 'content', 'image_src', 'byline']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
    else:
      fieldnames = ['main_section', 'sub_section', 'title', 'datetime', 'content', 'image_src', 'byline']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i in json_data_list:
      writer.writerow(i)
 

def parse_list(url0, url1, curDate):
  # use requests session
  session = requests.Session()
  is_next = ''
  data_cursor = ''
  data_page_no = 0
  for topicPage in range(1,300):
    target_url = f'https://news.naver.com/section/template/SECTION_ARTICLE_LIST_FOR_LATEST?sid={url0}&sid2={url1}&cluid=&pageNo={data_page_no+1}&date={curDate}'
    if is_next == 'false':
      break
    else:
      if data_cursor != '':
        res = session.get(url=target_url + f'&next={data_cursor}')
        soup = BeautifulSoup(res.text.replace('\\n','').replace('\\t','').replace('\\', ''), 'html.parser')
      else:
        res = session.get(url=target_url)
        soup = BeautifulSoup(res.text.replace('\\n','').replace('\\t','').replace('\\', ''), 'html.parser')
    
      # find persist_META  div class="section_latest_article _CONTENT_LIST _PERSIST_META
      metadata = soup.find('div', class_='section_latest_article _CONTENT_LIST _PERSIST_META')
      # data-has-next="true" data-cursor-name="next" data-cursor="2024051618114244187" data-page-no="2"
      if metadata['data-has-next'] == None:
        is_next = 'false'
      else:
        is_next = metadata['data-has-next']
      data_cursor = metadata['data-cursor']
      data_page_no = int(metadata['data-page-no'])
    
      newsList = soup.select('li')
      parse_detail(newsList, url0, url1, curDate)
      # l_data_list += json_list
      time.sleep(0.27)


# csv to dataframe
def to_dataframe(url0, url1, curDate):
  df_per_section = pd.DataFrame()
  for i in url1:
    df = pd.read_csv(f'{curDate}_news_{url0}_{i}.csv')
    df_per_section = pd.concat([df_per_section, df])
    os.remove(f'{curDate}_news_{url0}_{i}.csv')

  print(df_per_section.shape)
  # delete duplicate rows (title, content, byline)
  df_per_section.drop_duplicates(subset=['title', 'content', 'byline'], inplace=True)
  print(df_per_section.shape)

  # drop rows with Nan values (title, content)
  df_per_section.dropna(subset=['title', 'content'], inplace=True)
  print(df_per_section.shape)

  # save to csv
  df_per_section.to_csv(f'{curDate}_news_{url0}.csv', index=False)

for curDate in date_list: # from startdate to enddate
  for url in urls: # url[0] is main_section, url[1] is sub_section
    # parse list
    main_section = url[0]
    sub_section = url[1:]

    print("main_section : " + main_section)

    # do threading (better performance in I/O bound tasks)
    threads = []
    for i in sub_section:
      threads.append(threading.Thread(target=parse_list, args=(main_section, i, curDate)))
    for t in threads:
      t.start()
    for t in threads:
      t.join()
    
    # to dataframe
    to_dataframe(main_section, sub_section, curDate)
    print(f'{curDate} {main_section} done')


