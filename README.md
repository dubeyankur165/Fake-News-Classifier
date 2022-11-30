
# Fake News Detection



## Overview

The topic of fake news detection on social media has recently attracted tremendous attention. The basic countermeasure of comparing websites against a list of labeled fake news sources is inflexible, and so a machine learning approach is desirable. Our project aims to use machine learning algorithms and Natural Language Processing to detect fake news directly, based on the text content of news articles.
## Problem Statement

Develop a machine learning program to identify when a news source may be producing fake news. We aim to use a corpus of labeled real and fake new articles to build a classifier that can make decisions about information based on the content from the corpus. The model will focus on identifying fake news sources, based on multiple articles originating from a source
## Dataset Description

This contains data relevant for the 2016 US Presidential Election, including up-to-date primary results

train.csv: training Dataset has attributes id, title, author, text and label . It contains 20800 records on which we train our model

test.csv : test Dataset has attributes id, title, author, text the test dataset has 5200 records o which we test our model.

[Dataset From Kaggle](https://www.kaggle.com/datasets/benhamner/2016-us-election)


## Try It Out

1. Make sure you have all the dependencies installed-  
 * python 3.6+
 * numpy
 * wordcloud
 * seaborn
 * sklearn
 * pandas
 * nltk
   * For nltk, we recommend typing `python.exe` in your command line which will take you to the Python interpretor.  
     * Then, enter-
       * `>>> import nltk`
       * `>>> nltk.download()`}
    
2. To deploy this on flask make sure you install flask  
3. You are good to go now
 > python app.py
4. Enter the title, author ansd text then predict your news



## References

 * [Fake News Identification - Stanford CS229](http://cs229.stanford.edu/proj2017/final-reports/5244348.pdf)
 * [Dataset From Kaggle](https://www.kaggle.com/datasets/benhamner/2016-us-election)