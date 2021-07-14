
'''

							                    			Developing And Analysing A Hindi Corpus
									                       -----------------------------------------

														                            _A Mini Project By Shubham Pathak
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
_____________________________________________________________________________________________________________________________________________________________________________________________
                This code is to import all the text in the corpora and analyse it through the frequency distribution of the Bigrams and Trigramsand export the results to the excel file.

importing
Natural language toolkit : For Tokenising, removing stopwords And Frequency distribution.
cltk : for using its stopwords.
codec : Reading text with UTF-8. 
glob : To bring all the text files.
pandas : For making dataframes, analysis and exporting them in Excel 
'''
import nltk                                                                      
from nltk.probability import FreqDist
from cltk.tokenize.sentence import TokenizeSentence
import codecs
import string
import re 
from nltk.corpus import stopwords
from cltk.stop.classical_hindi.stops import STOPS_LIST
import pandas as pd
import glob
def rem_num(text):                                                              #Functon to remove numbers.
    pattern = '[0-9]'
    text = [re.sub(pattern, '', i) for i in text] 
    return text
def rem_punc(text):                                                             #Functon to remove Punctuations.
    mod_punc= string.punctuation + '।'
    text =[w for w in text if not w in mod_punc]
    return text
def open_file(path):                                                            #Functon to open files.
    t1=[]
    for text in path:
        with codecs.open(text,encoding='utf-8') as f:
            input_=f.read()
        t1.extend(token(input_))  
    return t1
def token(text):                                                                #Functon to Tokenize text.
    text = nltk.tokenize.word_tokenize(text) 
    return text
def rem_sw(text):                                                               #Functon to remove stopwords.
    stop_words = stopwords.words('hindi')
    text = [w for w in text if not w in stop_words + STOPS_LIST ]
    return text
def clean_text(text):                                                           #Functon to clean text completely.
    text=rem_num(text)
    text=rem_punc(text)
    text=rem_sw(text)
    return text
def freq_dist(text):                                                           #Functon to give frequency distribution.
    fdist= FreqDist(text)
    return fdist
def most_com(freqdis,x):                                                        #Functon to give most commons.
    mc=freqdis.most_common(x)
    return mc
def make_df(li):                                                                #Functon to make a dataframe.
    df= pd.DataFrame (li, columns =[ 'WORDS ' ,'FREQUENCY'])
    df.index= df.index+1
    return df

path=glob.glob(r"F:\HINDI_CORPUS\Corpora\Prabhat Khabar\*\*.txt")                             #Input the path.
text = open_file(path)                                                          #Getting the text. 
text = clean_text(text)                                                         #Cleaning the text.


#Create your bigrams
bgs = nltk.bigrams(text)
#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
mc_li=most_com(fdist,50)                                                        #Most common Bigrams.
li=[]
for k,v in list(fdist.items()):
    li.extend([k,v])
li_df= pd.DataFrame ( mc_li , columns =[ 'Words ' ,'Frequency'])                #Creating a dataFrame for all the Bigrams.
li_df.to_excel(r'F:\HINDI_CORPUS\Results\Frequency Distribution of 50 Most Common Bigrams(PK).xlsx', index = False, header= True) #Exporting to Excel.


#Create your Trigrams
tgs = nltk.trigrams(text)
#compute frequency distribution for all the Trigrams in the text
fdist = nltk.FreqDist(tgs)
mc_li=most_com(fdist,40)                                                        #Most common Trigrams.
li=[]
for k,v in list(fdist.items()):
    li.extend([k,v])
li_df= pd.DataFrame ( mc_li , columns =[ 'Words ' ,'Frequency'])                #Creating a dataFrame for all the Trigrams.
li_df.to_excel(r'F:\HINDI_CORPUS\Results\Frequency Distribution of 40 Most Common Trigrams(PK).xlsx', index = False, header= True) #Exporting to Excel.
