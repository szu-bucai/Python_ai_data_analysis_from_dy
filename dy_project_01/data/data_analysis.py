import sys
import os
from unittest import result
import pandas as pd
from sqlalchemy import create_engine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

engine=create_engine(f'mysql+pymysql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}?charset=utf8')

video_data=pd.read_sql_table('video_data',engine)
comment_data=pd.read_sql_table('video_comment',engine)

def part1():
  result1=comment_data['userIP'].value_counts().reset_index()
  result1.columns=['userIP','count']
  result1.to_sql('part1',engine,if_exists='replace',index=False)
  
def part2():
  result2=video_data[['likeCount','collectCount','commentCount','downloadCount','shareCount']]\
    .sort_values(by='likeCount',ascending=False)\
      
 
  result2['ratio']=result2['collectCount']/result2['likeCount']
  print(result2)
  result2.to_sql('part2',engine,if_exists='replace',index=False)

def part3():
  bins=[0,1000,10000,100000,1000000,float('inf')]
  labels=['小于1000','1000-10000','10000-100000','100000-1000000','大于1000000']
  video_data['fansRange']=pd.cut(video_data['fansCount'],bins=bins,labels=labels)

  result=video_data['fansRange'].value_counts().reset_index()
  result.columns=['fansRange','count']
  result.to_sql('part3',engine,if_exists='replace',index=False)
  print(result)

def part4():
  """
  粉丝数量排行
  """
  video_data_df=video_data[['username','fansCount']]
  result=video_data_df.drop_duplicates('username')
  result=result.sort_values(by='fansCount',ascending=False)
  result=result.head(10)
  print(result)
  result.to_sql('part4',engine,if_exists='replace',index=False)

def part5():
  """
  评论与分享
  """
video_data_df=video_data[['commentCount','shareCount','`describe`']]
result=video_data_df.sort_values(by='commentCount',ascending=False)
result.to_sql('part5',engine,if_exists='replace',index=False)
print(result)

if __name__=='__main__':
  part5()