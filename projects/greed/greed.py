import random
import math
import pr1testing
import myStrat1 
import strat2_mutatable
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
    diceTotal = 0
    diceString = ""
    i = n
    while i > 0:
        d = roll()
        diceTotal += d
        diceString = diceString + " " + str(d)
        i = i-1
    return diceTotal

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
        dieCount = strat1(score[1], score[2], isLast)
        thisTotal = rollMany(dieCount)
        score[1] += thisTotal
        print('player ', whoseTurn, ' rolled ', dieCount, ' die and scored ', thisTotal, ' points. scores: ', score)
        whoseTurn = 2
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
        dieCount = None
        thisTotal = None
        dieCount = strat1(score[1], score[2], isLast)
        thisTotal = rollMany(dieCount)
        score[1] += thisTotal

        dieCount = None
        thisTotal = None
        dieCount = int(strat2(score[2], score[1], isLast))
        thisTotal = rollMany(dieCount)
        score[2] += thisTotal
        if score[1] > 100 or score[2] > 100 or isLast == True:
            break
            gameOver = True
        if dieCount == 0:
            isLast = True
    return score

def manyGames(strat1, strat2, n):
    victories = {}
    victories[1] = 0
    victories[2] = 0
    victories[3] = 0
    for x in range(0, n):
        thisScores = autoplay(strat1, strat2)
        if thisScores[1] > 100:
            victories[2] += 1
        elif thisScores[2] > 100:
            victories[1] += 1
        elif thisScores[1] > thisScores[2]:
            victories[1] += 1
        elif thisScores[2] > thisScores[1]:
            victories[2] += 1
        else:
            victories[3] += 1
    # print(victories)
    if victories[1] > victories[2]:
        print('player 1 win')
    # elif victories[1] == victories[2]:
        # print('tie')
    # else:
        # print('player 2 win')
    return victories

# lastProb = 0
# lastAction = 'add'
# highThresh = 0
# highProb = 0.0
# normProb = 0.8
# prevResults = manyGames(strat2_mutatable.create(highThresh, highProb, normProb), pr1testing.test11, 1000)
# highest = 0
# while True:
#     for x in range(1, 95):
#         for y in range(1, 100):
#             highThresh = x
#             highProb = y / 100
#             results = manyGames(strat2_mutatable.create(highThresh, highProb, normProb), pr1testing.test11, 1000)
# 
#             if results[1] > highest:
#                 print(results[1], highThresh, highProb, normProb)
#                 highest = results[1]
#             if results[1] > results[2]:
#                 print('BAMMM', highThresh, highProb, normProb)
#                 break
#         print('completed ', x, ' numerspace')
# 
import multiprocessing
from multiprocessing import Pool
import logging
import time

threads = multiprocessing.cpu_count()

logging.basicConfig(filename= 'logs/' + str(time.time()) + '.log',level=logging.DEBUG)

def mutateToTenths(count):
    start = int((100 / threads) * (count - 1))
    stop = int((100 / threads) * count)
    highest = {}
    highest['score'] = 0
    for x in range(start, stop):
        for y in range(50, 90):
            for z in range(50, 90):
                highThresh = x
                highProb = y / 100
                normProb = z / 100
                results = manyGames(strat2_mutatable.create(highThresh, highProb, normProb), pr1testing.test11, 10000)
                if results[1] > highest['score']:
                    logging.debug(highest)
                    highest['score'] = results[1]
                    highest['highThresh'] = highThresh
                    highest['highProb'] = highProb
                    highest['normProb'] = normProb
    logging.debug(count, 'done. results:', highest)
    return highest

pool = Pool()
results = pool.map(mutateToTenths, [1,2,3,4])
logging.debug('the verdict is: ', results)
# pr1testing.testStrat(strat2_mutatable.create(56, 0.79, 0.8), 10000)
