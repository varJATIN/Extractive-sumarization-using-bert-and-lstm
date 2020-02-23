import numpy as np
import 
#batch_generation
def batchify(batch_size,df,seq_len):
  """ arguments will be dataframe column to batchify and batch_size
      returns a tensor containing all batches  
  """
  batch=torch.zeros(batch_size,seq_len)
  batches=[]
  for i in range(0,df.shape[0],batch_size):
    #print(batch.shape)
    #print(df.iloc[i:(i+batch_size)]) # .iloc last elemnet is not included .loc last element included
    batch=torch.tensor(df.iloc[i:(i+batch_size)].tolist())
    batches.append(batch)
  return batches
#padding
def padding(df,seq_len):
  """takes a column of the indexed_tokens, returns a column with 0 padding""" 
  count=0
  for i,j in enumerate(df):
    if (len(j)<=seq_len):
      df[i]=j+[0]*(seq_len-len(j))# adds the 0's in the list
      count+=1
    else :#(len(j)>=seq_len):
      df[i]=j[:seq_len]
  print(count)
  return df

# seg _id generation
def segment_id_gen(df):
  """recieves a df and returns the seg_id for each sample """ 
  seg_ids=[]
  for i in df:
    seg_id=[]
    count=0
    for j in i:
      if j==101:
        count+=1
      if count%2==0:
        k=[1]
      else:
        k=[0]
      seg_id+=k
      # print(j)
    seg_ids+=[seg_id]
  print((seg_ids[2]))
  return seg_ids




if main:
  batch_size=10
  seg_ids=segment_id_gen(raw_news['indexed_text'])
  raw_mains['cls_ind']=padding(raw_news['cls_ind'],max_sent_summ)
  batches=batchify(batch_size,raw_news['indexed_text'],512)
  cls_batch=batchify(batch_size,raw_news['cls_ind'],max_sent_summ)
