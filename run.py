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
    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(completed_word "\n")
    
    
    while not guess and attempts > 0:
        """
        Compares players guess against the correct word
        """
        guess = input("please enter a letter or word: \n").upper()
        if len(guessed) == 1 and guess.isalpha():
            if guessed in letters_guessed:
                print("you've guessed that letter already", guessed)
            elif guessed not in word:
                print("Sorry,", guessed "is not in the word\n")


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
