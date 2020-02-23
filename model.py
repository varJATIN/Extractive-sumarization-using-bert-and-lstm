class BertSumExt(nn.Module):
  def __init__(self,max_no_sent,max_no_sent_sum):
    super(BertSumExt, self).__init__()
    self.bert= BertModel.from_pretrained('bert-base-uncased')
    self.lstm1=nn.LSTM(768,512,2)
    self.incl_sent=nn.Linear(512,max_no_sent_sum)
  def forward(self,input_token,seg_id,cls_ind,max_no_sent):
    output,_=self.bert(input_token,seg_id)
    #y=[j for j in output[0]] 
    y=torch.zeros(10,max_no_sent,768)   #cls_ind shape is 10*41
    for i,tensor in enumerate(output[0]):
      k=0
      for j,ids in enumerate(cls_ind[i]):
        if ids!=0:
          y[i,k,:]=output[0][i,ids,:]
          k+=1
    output=self.lstm1(y)
    output=self.incl_sent(output)
