import nltk 
from nltk.probability import FreqDist
import codecs
with codecs.open("F:\HINDI_CORPUS\AU\AU-2020-APR\AU-2020-APR-01.txt",encoding='utf-8') as f:
    input_=f.read()
t1 = []
t1= nltk.tokenize.word_tokenize(input_)
fdist=FreqDist(t1)
import pandas as pd 
df= pd.DataFrame (list(fdist.items()), columns =[ 'WORDS ' ,'FREQUENCY'])
print(df)