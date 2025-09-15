
import sys
import os

import matplotlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
import pymysql
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba



conn=pymysql.connect(
  host=Config.DB_HOST,
  user=Config.DB_USER,
  password=Config.DB_PASSWORD,
  database=Config.DB_NAME,
  charset='utf8'
)
cursor=conn.cursor()

matplotlib.use('TkAgg')

def video_title_wordcloud():
  sql='select `describe` from video_data'
  cursor.execute(sql)
  result=cursor.fetchall()
  text=''
  for row in result:
    if row and row[0]:  # 检查row存在且row[0]不为None
      text += str(row[0]) + ' '

  data_cut=jieba.cut(text,cut_all=False)
  word_text=' '.join(data_cut)
  wordcloud=WordCloud(
    width=800,
    height=800,
    background_color='white',
    font_path='simhei.ttf',
    max_words=300,
    max_font_size=100,
    min_font_size=10,
    collocations=False,
    prefer_horizontal=0.8,
  ).generate(word_text)

  plt.figure(figsize=(10,10))
  plt.imshow(wordcloud,interpolation='bilinear')
  plt.axis('off')
  plt.show()
  # plt.savefig('video_title_wordcloud.png')

video_title_wordcloud()


def comment_wordcloud():
  sql='select comment_content from video_comment'
  cursor.execute(sql)
  result=cursor.fetchall()
  text=''
  for row in result:
    if row and row[0]:
      text += str(row[0]) + ' '
  data_cut=jieba.cut(text,cut_all=False)
  word_text=' '.join(data_cut)
  wordcloud=WordCloud(
     width=800,
    height=800,
    background_color='white',
    font_path='simhei.ttf',
    max_words=300,
    max_font_size=100,
    min_font_size=10,
    collocations=False,
    prefer_horizontal=0.8,
  ).generate(word_text)

  plt.figure(figsize=(10,10))
  plt.imshow(wordcloud,interpolation='bilinear')
  plt.axis('off')
  plt.show()