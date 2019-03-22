#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
import collections

def word_counter(text, language = 'english'):
    
    if(type(text) is not str or type(language) is not str):
        raise(TypeError)
        
    try:
        stop_words = set(stopwords.words(language))
    except:
        raise(TypeError)
        
    punctuation_marks = ["?", "¿", "¡", "!", " ", ",", ".", ";", ":"]
    filtred_text = ""
    
    for letter in text:
        if(letter not in punctuation_marks):
            filtred_text = filtred_text + letter
        else:
            filtred_text = filtred_text + " "
        
    filtred_text = filtred_text.lower().split()
    
    result_words = []
    
    for word in filtred_text:
        if(word not in stop_words):
            result_words.append(word)
            
    if(len(result_words) == 0):
        return None
    
    return collections.Counter(result_words)


def run():
    """Entry point for console_scripts
    """

if __name__ == "__main__":
    run()
