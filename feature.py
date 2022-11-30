import numpy as np # linear algebra
import pandas as pd #data processing
from nltk.stem import WordNetLemmatizer


import os
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
def get_all_query(title, author, text):
    total= title + author + text
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence):
    filter_sentence = ''
    lemmatizer=WordNetLemmatizer()
    sentence = re.sub(r'[^\w\s]','',)
    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stopwords]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
