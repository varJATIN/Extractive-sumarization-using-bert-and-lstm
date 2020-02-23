#now we need to insert ['cls'] and ['sep']
import convert_to_ids
def add_cls_sep(raw_news):
  count=0
  cls=[]
  max_no_sent=0
  for j in raw_news['indexed_text']:
    j.insert(0,101)
    cls_ids=[]
    cls_ids.append(0)
    num=0
    #[(cls_ids.append(i+2),j.insert(i+1,102),j.insert(i+2,101),num=num+1) for i,k in enumerate(j,0) if k == 1012]
    for i,k in enumerate(j,0):
      if k == 1012:
        j.insert(i+1,102)
        j.insert(i+2,101)
        if (i+2)!= len(j): # to avoid inserting cls tokwn aT THE end of sentence
          cls_ids.append(i+2)
        num=num+1
    #try:
    if len(j)>256:
      count+=1
    cls.append(cls_ids)
     # pos=j.index(1012)
      #j.insert(pos+1,102)  #it has a drawback that it returns first index only
      #j.insert(pos+2,101)
    #except:
      #count+=1
    if j[-1]==101: #rmove cls token inserted at the end
      j.pop(-1)
    
  return cls
#give raw_news after 4
cls=add_cls_sep(raw_news)
raw_news['cls_ind']=cls

