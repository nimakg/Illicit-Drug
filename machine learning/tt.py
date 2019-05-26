import nltk
import tkMessageBox
from Tkinter import *
import pandas as pd
import numpy as np
import time
from tkFileDialog import *
import pickle
root=Tk()
root.withdraw()
def get_words_in_sentences(sentences):
            all_words = []
            for (words, sentiment) in sentences:
                    all_words.extend(words)
            return all_words

	
def get_word_features(wordlist):
            wordlist = nltk.FreqDist(wordlist)
            word_features = wordlist.keys()
            return word_features

def mainn():
    train = pd.read_csv("out1.csv", header=0,delimiter=",", quoting=1)
    num_reviews = train["statements"].size
    print num_reviews
    data=[]
    sentiments=[]
    global sentences
    sentences = []
    for i in xrange( 0,num_reviews ):
        sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',train["statements"][i])
        sente = re.sub('@[^\s]+','',sente)    
        sente = re.sub('[\s]+', ' ', sente)
        sente = re.sub(r'#([^\s]+)', r'\1', sente)
        sente = sente.strip('\'"')
        words_filtereds = [e.lower() for e in sente.split() if len(e) >= 3]
        sentences.append((words_filtereds,train["sentiments"][i]))

    word_features = get_word_features(get_words_in_sentences(sentences))
    
    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
          features['contains(%s)' % word] = (word in document_words)
        return features
    print sentences
    tkMessageBox.showinfo("Training Completed","Training Completed")
    training_set = nltk.classify.util.apply_features(extract_features, sentences)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    f=open("myclass.pickle","wb")
    pickle.dump(classifier,f)
    f.close
    tkMessageBox.showinfo("Training Completed","Training Completed")
