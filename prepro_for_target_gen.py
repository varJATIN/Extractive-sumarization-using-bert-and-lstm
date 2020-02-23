import os
import regex as re
import pandas as pd
directory='/content/drive/My Drive/bbc news/'
#
def read(directory,folder):
  if (folder=='news'):
    select='News Articles'
  elif (folder=='summary'):
    select='Summaries'
  else:
    select=folder
  x=os.path.join(directory,select)
    #print(x)
  ls=[]
  for files in sorted(os.listdir(x)):
    y=os.path.join(x,files)
    #print(y)
    fil_1='001'
    for fil in sorted(os.listdir(y)):
      z=(os.path.join(y,fil))
      #print((fil[:3]+' (1)'))
      if((fil[:3]+' (1)')!=fil_1):# to remove he same files being read twice
       # print(z)
        try:
          with open(z,'r') as f: # you can use 'rb' to read file as byte type not str type
            a=f.read()
        except:
          with open(z,encoding= 'unicode_escape') as f: #in case there is a char that can't be decoded by utf-8
            a=f.read()
        a = re.sub(r'\n','.',a)
        #x=re.sub('..','.',x) #it is removing all the chars
        a=a.replace('..','.')
        a=a.replace('..','.')
        a=a.split('.')
        ls.append(a)  
      fil_1=fil[:7]
  return ls
  
news=read(directory,'News Articles')
summary=read(directory,'summary')

if(len(news)==len(summary)):
  target=[]
  max_sen_news=0
  max_sen_summ=0
  for news_a,sum_a in zip(news,summary):
    sent_sel=[]
    for i in sum_a:
      for j,sen in enumerate(news_a):
        if sen.strip() == i.strip() :
          sent_sel.append(j)
        if max_sen_news<j:
          max_sen_news=j  
    if max_sen_summ<len(one_hot):
      max_sen_summ=len(one_hot)
  target.append(one_hot)  
else:
  print("error while loading")  

data=pd.DataFrame()
data['news']=news
data['summary']=summary
data['target']=target
#saving the generated labels
data.to_csv('/content/drive/My Drive/bbc news/processed.csv')
