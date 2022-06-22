import random
from words.py import list_of_words

def get_words():
    """ 
    Generates random word from word.py
    """
    word = random.word(list_of_words)
    return word.upper()