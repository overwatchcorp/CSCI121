import random
import math
import pr1testing
random.seed()

# CSCI 121 Fall 2017
# 
# Project 1: Game of Greed starting code.
#
# See the project description on the web.
# 
# You can play an game of Greed with an opponent by running 
# something like the following in the terminal:
#
#     python3 -i greed.py
#     >>> play()
#
# This 'play' function will ask for your two names, and then
# offer Player 1 to take a turn, then Player 2, etc.
#
# Several function templates follow, ones that you are asked
# to complete for this assignment.
#
# You'll turn this in at the cs.reed.edu CSHW/VRFY submission
# site.
#

def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1? ")
    player2 = input("Name of Player 2? ")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print("It is " + player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll? "))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        print("Dice rolled:" + diceString)
        print("Total for this turn: " + str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print("It is " + player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll? "))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        print("Dice rolled:" + diceString)
        print("Total for this turn: " + str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2):
    #your code here
    return ___

def autoplay(strat1, strat2):
    #your code here
    return ___

def manyGames(strat1, strat2, n):
    #your code here
    return ___

def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
       return 12

def sample2(myscore, theirscore, last):
    #your code here
    return ___

def improve(strat):

    def new_strat(myscore, theirscore, last):
        #your code for 'new_strat' here, improving
        #the move of 'strat'
        return ___

    return new_strat

def myStrategy(myscore, theirscore, last):
    #your code here
    return ___

