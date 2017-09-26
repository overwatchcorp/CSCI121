import random
import math
import pr1testing
import myStrat1 
import strat2
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

def rollMany(n):
    total = 0
    for x in range(0, n):
        total += roll()
    return total

def autoplayLoud(strat1, strat2):
    gameOver = False
    score = {}
    score[1] = 0
    score[2] = 0
    whoseTurn = 1
    isLast = False
    while gameOver != True:
        # print('it\'s player ', whoseTurn, '\'s turn. their score is ', score[whoseTurn]) 
        dieCount = None
        thisTotal = None
        if whoseTurn == 1:
            dieCount = strat1(score[1], score[2], isLast)
            thisTotal = rollMany(dieCount)
            score[1] += thisTotal
            print('player ', whoseTurn, ' rolled ', dieCount, ' die and scored ', thisTotal, ' points. scores: ', score)
            whoseTurn = 2
        else:
            dieCount = int(strat2(score[2], score[1], isLast))
            thisTotal = rollMany(dieCount)
            score[2] += thisTotal
            print('player ', whoseTurn, ' rolled ', dieCount, ' die and scored ', thisTotal, ' points. scores: ', score)
            whoseTurn = 1
        if score[1] > 100:
            print('player 1 overshot!')
            gameOver = True
        elif score[2] > 100:
            print('player 2 overshot!')
            gameOver = True
        elif isLast == True:
            print('all turns up.')
            gameOver = True
        if dieCount == 0:
            print('player ', whoseTurn, ' passed.')
            isLast = True
    print('final scores: player 1: ', score[1], ' player 2: ', score[2])
    return score 

def autoplay(strat1, strat2):
    gameOver = False
    score = {}
    score[1] = 0
    score[2] = 0
    whoseTurn = 1
    isLast = False
    while gameOver != True:
        # print('it\'s player ', whoseTurn, '\'s turn. their score is ', score[whoseTurn]) 
        dieCount = None
        thisTotal = None
        if whoseTurn == 1:
            dieCount = strat1(score[1], score[2], isLast)
            thisTotal = rollMany(dieCount)
            score[1] += thisTotal
            whoseTurn = 2
        else:
            dieCount = int(strat2(score[2], score[1], isLast))
            thisTotal = rollMany(dieCount)
            score[2] += thisTotal
            whoseTurn = 1
        if score[1] > 100 or score[2] > 100 or isLast == True:
            gameOver = True
        if dieCount == 0:
            isLast = True
    return score

def manyGames(strat1, strat2, n):
    victories = {}
    victories[1] = 0
    victories[2] = 0
    for x in range(0, n):
        thisScores = autoplayLoud(strat1, strat2)
        if thisScores[1] > thisScores[2]:
            victories[1] += 1
        else:
            victories[2] += 1
    print(victories)
    return victories

def sample1(myscore, theirscore, last):
    if myscore == 0:
        return 28
    if myscore > theirscore:
        return 0
    else:
       return 12

def sample2(myscore, theirscore, last):
    #blah blah blah
    return __

def improve(strat):

    def new_strat(myscore, theirscore, last):
        #your code for 'new_strat' here, improving
        #the move of 'strat'
        return ___

    return new_strat

def myStrategy(myscore, theirscore, last):
    #your code here
    return ___

manyGames(strat2.create(False), pr1testing.test7, 1)
# pr1testing.testStrat(strat2.create(True), 2)
