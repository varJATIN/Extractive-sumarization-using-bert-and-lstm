import raw_read
import pandas as pd
import tokenizer
#load
raw=raw_read('/content/drive/My Drive/bbc news/News Articles')
raw_news['news']=raw
#tokenize
processed_text=[]
text_cnt=[]
for i in raw_news['news']:
  i=tokenizer.tokenize(i)
  processed_text.append(i)
  text_cnt.append(len(i))
  
#
data=pd.read_csv('processed.csv')
raw_news['processed_text']=processed_text
raw_news['text_cnt']=text_cnt
raw_news['target']=data['target']
