#
import load_news_and_tokenize

#
raw_news=raw_news.query('text_cnt<400 ') # to keep the final count to bert with input length<512
raw_news=raw_news.reset_index()
del raw_news['index']
for i in raw_news['processed_text']:
  indexed_text.append(tokenizer.convert_tokens_to_ids(i))
raw_news['indexed_text']=indexed_text


