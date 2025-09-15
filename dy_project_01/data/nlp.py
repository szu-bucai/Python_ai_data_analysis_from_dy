import pandas as pd
import jieba
from snownlp import SnowNLP

def noldemo(df):
  with open('stopwords.txt','r',encoding='utf-8') as f:
    stopwords=[line.strip() for line in f.readlines()]

  scores=[]
  segmented_comments=[]

  for comment in df['comment_content']:
    comment=str(comment)

    words=jieba.cut(comment)

    filtered_words=[word for word in words if word not in stopwords] 

    filter_text=''.join(filtered_words)
    segmented_comments.append(''.join(filter_text))
    if not filter_text.strip():
      scores.append(0.5)
    else:
      s=SnowNLP(filter_text)
      scores.append(s.sentiments)

  df['scores']=scores
  df['segmented']=segmented_comments

if __name__=='__main__':
  df=pd.read_csv('comment_data.csv')