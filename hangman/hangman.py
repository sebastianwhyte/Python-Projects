# Hangman made by Sebastian Whyte, 01/2021

import random
from hangmanStages import hangmanBody


# Program selects a word randomly from list of words
wordList = [ "code", "language", "python", "computer", "programming" ]
answer = random.choice( wordList )

right_letters = [ ]
used_letters = [ ]

wrongAttempts = 0

print("Let\'s play hangman!")

# Game function
def game():

    global wordList
    global answer
    global right_letters
    global used_letters


    letters = list( set( answer ) )


    if guess in answer:
        print("\n" + guess + " is in the answer!")
        letters.remove(guess)
        right_letters.append(guess)
        used_letters.append(guess)

        if len( set( answer ) ) == len( right_letters ):
            print( answer )
            print( "You won!" )
            quit()


    elif guess not in answer:
        print( "\n Sorry, " + guess + " is not in the answer." )
        used_letters.append( guess )
        print("Wrong Attempts: " + str(wrongAttempts) )

        if wrongAttempts == 1:
            print( hangmanBody[ 0 ] )

        if wrongAttempts == 2:
            print( hangmanBody[ 1 ] )

        if wrongAttempts == 3:
            print( hangmanBody[ 2 ] )

        if wrongAttempts == 4:
            print( hangmanBody[ 3 ] )

        if wrongAttempts == 5:
            print( hangmanBody[ 4 ] )

        if wrongAttempts == 6:
            print( hangmanBody[ 5 ] )

        if wrongAttempts == 7:
            print( hangmanBody[ 6 ] )
            print( "Too bad. The answer was: " + answer )
            quit()


# This will iterate dashes for each character in "answer". If guess is right, it will remove dash
def wordCensor():
    print("\n" + ' '.join(i if i in right_letters else '-' for i in answer) + "\n")


# Gets user guess and checks criteria
def getGuess():

    global guess
    global wrongAttempts


    while len( set( answer ) ) != len( right_letters ):
        wordCensor()

        guess = input( "Please type only one letter: " )

        if guess not in answer and wrongAttempts < 7:
            wrongAttempts += 1


        if len(guess) == 1:
            if guess.isalpha():
                game()

        elif len(guess) !=1 or guess.isdigit():
            print("Invalid input. Try again.")

getGuess()
