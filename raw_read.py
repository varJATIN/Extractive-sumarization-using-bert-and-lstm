def raw_read(directory):
  ls=[]
  for files in sorted(os.listdir(directory)):
    y=os.path.join(directory,files)
    fil_1='001'
    for fil in sorted(os.listdir(y)):
      z=(os.path.join(y,fil))
      if((fil[:3]+' (1)')!=fil_1):# to remove he same files being read twice
        try:
          with open(z,'r') as f: # you can use 'rb' to read file as byte type not str type
            a=f.read()
        except:
          with open(z,encoding= 'unicode_escape') as f: #in case there is a char that can't be decoded by utf-8
            a=f.read()
        a = re.sub('\n','.',a)
        #x=re.sub('..','.',x) #it is removing all the chars
        a=a.replace('..','.')
        a=a.replace('..','.')
        ls.append(a)  
      fil_1=fil[:7]
  return ls
