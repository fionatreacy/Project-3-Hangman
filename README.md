# Portfolio 3: Hangman

This interactive game of Hangman is a simple CLI game which runs on the Code Institute mock terminal on Heroku. Players must guess letters or words until they either are correct and win, or run out of attempts and the hangman gets executed.

<a href="https://portfolio-3-hangman.herokuapp.com/" target="_blank" rel="noopener">Here is the live version of my project</a>

----

## How to Play

Hangman is a classic pen and paper game

Originally played with 2 or more players where one thinks of a word and the others guess, this version can be played solo as the computer randomly generates a word

The player can guess a letter or a 5-letter word

If they guess a correct letter, they are shown where the guessed letter fits in the word. If they are wrong, the lose an attempt and the hangman figure updates to show he is closer to execution

If they guess the correct word they are congratulated on their win and asked if they would like to play again

If they run out of attempts, they are told what the word is and asked if they would like to play again

----

## Features

* Intro

When loaded the game welcomes the user and explains the game

![game intro](/images/hangman-intro.png)

* Input validation and error checking

Player can't enter invalid guesses such as numbers or words that aren't 5 letters, and can't guess the same letter twice

![invalid guess](/images/invalid-guess.png)

* End of game

When the game concludes it congratulates the player on their win, or displays the executed hangman along with the correct word. In both instances it asks the player if they'd like to play again

![end of game](/images/game-conclusion.png)

## Future Features

* Add graphics to game
* Options to chose easy, medium or hard mode, with different length words and different amounts of attempts

----

## Flowchart

![flowchart](/images/flowchart.png)

----

## Testing

I've manually tested my project by doing the following:

* Passing it through the PEP8 linter, which found no significant problems except one line being 4 characters too long
* Entered invalid inputs
* Tested in both the Code Institute Heroku terminal and my own GitHub terminal on multiple laptops and computers

## Bugs

* When I originally passed my code through the PEP8 linter is found multiple lines that were too long or contained whitespace, which I fixed and removed
* When players lost the game would tell them that they won, I fixed this by finding a bug in my if, else conditions

## Remaining Bugs

* No remaining bugs, one line is too long but doesn't negatively affect gameplay. Any attmepts to shorten the line have negatively impacted both the surrounding code and gameplay

-----

## Deployment

This project was deployed using Code Institutes mock terminal on Heroku. The steps for deployment are as follows:

* Clone or fork this repository
* Create a new Heroku app
* Add necessary config vars, in my case PORT 8000
* Add buildpacks Python and NodeJS, in that order
* Link the Heroku app to the correct repository
* Click DEPLOY

----

## Credits

* Code Institute for the deployment terminal
* I referred to tutorials by Kite ("How to Build Hangman with Python in 10 Minutes") and Tech with Tim ("5 Mini Python Games for Beginners") and CS Students ("How to Build a Hangman Game with Python"). I got the code for my hangman figure in my display_hangman function from Kite's tutorial.