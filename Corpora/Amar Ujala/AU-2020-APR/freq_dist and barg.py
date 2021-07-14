#This code is to write the tokenised data and analyse it through its frequency distribution.
#It will import all the News of Amar Ujala (April 2020).
import nltk                                                                      #Importing Natural language toolkit
from nltk.probability import FreqDist 
import codecs                                                                    #To decode the hindi text files.
import glob                                                                      #To call all the files in sequence.
import pandas as pd 
t1 = []            
for text in glob.glob("F:\HINDI_CORPUS\AU\AU-2020-APR\*.txt"):
    with codecs.open(text,encoding='utf-8') as f:
        input_=f.read()
    t1.extend(nltk.tokenize.word_tokenize(input_))                           #To tokenize text and store.
print(t1)                                                                        #Printing tokenised text. 

fdist=FreqDist(t1)                                                               #To get frequency distribution.

df= pd.DataFrame (list(fdist.items()), columns =[ 'WORDS' ,'FREQUENCY'])        #Creating a dataframe.
df                                                                               #Printing the dataframe.
Bgraph = df.plot.barh(x='WORDS',y='FREQUENCY')                                      #Ploting data in graph