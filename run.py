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
        and returns message if guess is right, wrong, or already guessed
        """
        guess = input("please enter a letter or word: \n").upper()
        if len(guessed) == 1 and guess.isalpha():
            if guessed in letters_guessed:
                print("you've guessed that letter already", guessed)
            elif guessed not in word:
                print("Sorry,", guessed "is not in the word\n")
                attempts -= 1
                letters_guessed.append(guessed)
            else:
                print("Congrats, you've guessed a correct letter!")
                letters_guessed.append(guessed)
                word_converted_to_list = list(completed_word)
                indices = [i for i, letter in enumerate(word) if letter == guessed]
                for index in indices:
                    word_as_list[index] = guess
                completed_word = "".join(word_as_list)
                if "_" not in completed_word:
                    guess = True


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
