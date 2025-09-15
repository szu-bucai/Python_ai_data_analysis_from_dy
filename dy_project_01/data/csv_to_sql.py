import pandas as pd
import pymysql
import sys
import os
import re

# 添加父目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

def clean_text(text):
    """清理文本，移除表情符号和特殊字符"""
    if text is None:
        return None
    if isinstance(text, str):
        # 移除表情符号和其他4字节UTF-8字符
        return re.sub(r'[^\u0000-\uFFFF]', '', str(text))
    return text

conn=pymysql.connect(
  host=Config.DB_HOST,
  user=Config.DB_USER,
  password=Config.DB_PASSWORD,
  database=Config.DB_NAME,
  charset='utf8'
)

cursor=conn.cursor()

def save_video_info():
  # 注意：数据库表有id字段(自增)，所以不需要插入id
  # describe是MySQL保留字，需要用反引号包围
  sql='insert into video_data(username,fansCount,`describe`,videoId,createTime,videoTime,likeCount,collectCount,commentCount,downloadCount,shareCount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
  
  df = pd.read_csv('data.csv')
  # 将NaN值替换为None
  df = df.where(pd.notnull(df), None)
  
  for index, row in df.iterrows():
    cursor.execute(sql, (
      clean_text(row['用户名']), row['粉丝数量'], clean_text(row['视频描述']), row['视频id'], 
      clean_text(row['发表时间']), clean_text(row['视频时长']), row['点赞数量'], row['收藏数量'], 
      row['评论数量'], row['下载数量'], row['分享数量']
    ))

  conn.commit()
  cursor.close()
  conn.close()


def save_comment_info():
  # 修正表名为 video_comment (从models.py中的Meta.db_table)
  sql='insert into video_comment(user_id,user_name,comment_time,ip_address,comment_content,like_count,video_id) values(%s,%s,%s,%s,%s,%s,%s)'

  # 创建新的数据库连接，避免连接冲突
  comment_conn = pymysql.connect(
    host=Config.DB_HOST,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_NAME,
    charset='utf8'
  )
  comment_cursor = comment_conn.cursor()
  
  df = pd.read_csv('comment_data.csv')
  df = df.where(pd.notnull(df), None)

  for index, row in df.iterrows():
    comment_cursor.execute(sql, (
      clean_text(row['用户id']), clean_text(row['用户名']), clean_text(row['评论时间']), 
      clean_text(row['IP地址']), clean_text(row['评论内容']), row['点赞数量'], row['视频id']
    ))
  
  comment_conn.commit()
  comment_cursor.close()
  comment_conn.close()

if __name__=='__main__':
  save_video_info()
  save_comment_info()