
'''

							                    			Developing And Analysing A Hindi Corpus
									                       -----------------------------------------

														                            _A Mini Project By Shubham Pathak
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
_____________________________________________________________________________________________________________________________________________________________________________________________
                This code is to import all the text in the corpora and analyse it through the keywords occuring in the corpora and export the results to the text file.

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

path=glob.glob("F:\HINDI_CORPUS\CORPORA\*\*\*.txt")                             #Input the path.
text = open_file(path)                                                          #Getting the text. 
text = nltk.Text(text)
wordlist = text
ngrams = [wordlist[i:i+15] for i in range(len(wordlist)-14)]     #Creating 10-grams

kwicdict = {}                                                   #a Dictionary for keywords.
for n in ngrams:
    if n[7] not in kwicdict:
        kwicdict[n[7]] = [n]
    else:
        kwicdict[n[7]].append(n)
keys = [ 'मरीज','कोरोना','वायरस','मामले','संख्या','संक्रमण','देश','मौत']                                #Assigning the keywords.
kl= ', '.join(keys)
outF = codecs.open("F:\HINDI_CORPUS\keywords in the context.txt", "w" , 'utf-8')                   #Listing the names in file.
outF.write('This file contains concordance of '+ kl + ' in corpus :\n\n\n')
outF.write("\n")

num=1
for x in keys:    
    outF.write(str(num)+'. '+x + ' in corpus :\n\n\n')                                             #Heading before a praticular keyword.
    count=0
    outF.write("\n")
    for n in kwicdict[x]:
        outstring = ' '.join(n[:7]).rjust(40)                #words before the keywords:with right margin.
        outstring += str('*'+n[7]+'*').center(len(n[2])+50)          #keyword with center margin
        outstring += ' '.join(n[8:]).ljust(40)                         #text behind the keyword;with left margin.
        count= count + 1
        outF.write(outstring)                                                                       #Printing a complete line of a keyword.
        outF.write("\n")
    outF.write('\n\n The number of lines for ' + x + '  are = '+ str(count)+' .\n\n')               #For printing the numbers of lines.
    num=num+1
outF.close()
