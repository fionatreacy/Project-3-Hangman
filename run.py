import random
from words.py import list_of_words

def get_words():
    """ 
    Generates random word from word.py
    """
    word = random.word(list_of_words)
    return word.upper()

def play(word):
    """
    Displays game visuals including the hangman, number of attempts, incorrect guesses, and guessed words
    """
    completed_word = "_" * len(word)
    guess = False
    letters_guessed = []
    words_guessed = []
    attempts = 6


def display_hangman(attempts):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
