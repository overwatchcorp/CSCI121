# from scipy.stats import norm
import pr1testing
# import myStrat1 
# import strat2_mutatable
# import strat2

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
    # function that reduces reptition.
    # takes loop from play() and takes parameter for number of die, returns the total points for that roll
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
    # verbose function that prints progress to console each turn
    # useful for debugging
    gameOver = False
    score = {}
    score[1] = 0
    score[2] = 0
    whoseTurn = 1
    isLast = False
    while gameOver != True:
        print('it\'s player ', whoseTurn, '\'s turn. their score is ', score[whoseTurn]) 
        # dieCount and thisTotal are re-assigned between player 1 and player 2's turn
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
    # functionally identical to autoplayLoud, without prints
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
    # victories[1]: player 1 victories
    # victories[2]: player 2 victories
    # victories[3]: ties
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
    print('Player 1 Wins: ', victories[1])
    print('Player 2 Wins: ', victories[2])
    print('Ties: ', victories[3])
    # print(victories)
    # if victories[1] > victories[2]:
    #     print('player 1 win')
    # # elif victories[1] == victories[2]:
    #     print('tie')
    # else:
    #     print('player 2 win')
    return victories

def strategy1(risk, verbose):
    '''
    returns function that can be used to play risk
    strategy1 takes 2 paramters
    risk, float, % of times, on average, strat should overshoot 100 (risk of overshooting)
    verbose, boolean, if true strategy will print actions to console
    '''
    def play(myScore, theirScore, isLast):
        remainingScore = 100 - myScore
        print('remaining: ', remainingScore) if verbose == True else None
        # cap is the hgihest number of die that one could roll, given the mean of the die
        cap = int(remainingScore / dieMean)
        # we init maxSafe with the highest number of die, but we will deincrement until a safe number is found
        maxSafe = cap
        searching = True
        currentRisk = risk
        if theirScore > 95:
             currentRisk += risk * 10
        while searching:
            check = maxSafe
            mean = dieMean * check
            deviation = numpy.sqrt(dieVariance * check)
            zScore = (remainingScore - mean) / deviation
            # uses scipy.stats.norm to calculate probability from z score
            overshootOdds = norm.sf(zScore)
            print('checked: ', check, ' overshoot prob: ', overshootOdds, zScore) if verbose == True else None
            if overshootOdds < currentRisk:
                maxSafe = check
                searching = False
            else:
                maxSafe -= 1
            if maxSafe <= 0:
                break
        return maxSafe
    return play

def improve(strat):
    def better_strat(myScore, theirScore, isLast):
        # adding a function that made one last move if the opponent was bound to win was simple, but very effective and boosted my wins ~10% in some instances.
        if myscore < thierScore and myScore > 95:
            return 1
        return strat(myScore, theirScore, isLast)
    return better_strat


dieMean = 2.5
dieVariance = 2.9166666666667

def myStrategy(myScore, theirScore, isLast):
    '''
    magically, this strategy works a lot better
    if my score is less than 70, divide the remaining score (100 - myScore) by the mean of a die roll and multiply by a multiplier (chosen mildly randomly--I just fiddled around with the numbers for a while
    if my score is more than 70, do the same thing but use a slightly lower multiplyer
    if my score is less than my opponent's score AND my score is greater than 95, roll 1 die
    '''
    remainingScore = 100 - myScore
    if theirScore > myScore and myScore > 95:
        return 1
    if myScore < 70:
        return int(remainingScore / dieMean * 0.86)
    return int(remainingScore / dieMean * 0.80) 

pr1testing.testStrat(myStrategy, 10000)

'''
Strategy "Beat 11 at All Costs"
------------------------------
the following commented out code block is a script to attempt to brute force the optimal variables to beat test 11, the only test I couldn't beat with my strategy.
it is three nested for loops. from upper to inner:
    1. goes from integers start to stop. integer values are calculated by dividing 100 by the number of threads the computer has. we create a range of intergers to iterate over for eacth threads. ex on a 4 core machine, 0-25, 26-50, 51-75, 75-100. it does go into the negatives but this was a bit of a rush-job so it's not pefect. 
    this interger is the percent through 100 that the game switches from the early to late game multiplier
    2. go from .5 to .9, with steps of 0.01. this is to attempt to find the best 'early multiplier,' the multiplier used in the first (about) half of the game
    3. go from .5 to .9, with steps of 0.01. this is to find the late game multiplier

    inside loop 3, the script plays a number of games against strategy 11, using the for loop values as the parameters. 
    if the paramaters are score a higher number of wins than previous stratagies, the paramaters are written to the "highest" object
    at the end the highest object is returned

this process happens as many times as there are threads on the system.
running on a 12 core machine, I think this would have finished in about eight hours. I did beat stratagy 11 a few times, but I couldn't replicate it :)
'''

# def create(highThresh, highProb, normProb):
#     def strategy(myScore, theirScore, isLast):
#         remainingScore = 100 - myScore
#         if theirScore > myScore and myScore > 95:
#             return 1
#         if myScore < highThresh:
#             return int(remainingScore / dieMean * highProb)
#         return int(remainingScore / dieMean * normProb) 
#     return strategy
# import multiprocessing
# from multiprocessing import Pool
# import logging
# import time
# 
# threads = multiprocessing.cpu_count()
# 
# logging.basicConfig(filename= 'logs/' + str(time.time()) + '.log',level=logging.DEBUG)
# 
# def mutateToTenths(count):
#     start = int((100 / threads) * (count - 1))
#     stop = int((100 / threads) * count)
#     highest = {}
#     highest['score'] = 0
#     for x in range(start, stop):
#         for y in range(50, 90):
#             for z in range(50, 90):
#                 highThresh = x
#                 highProb = y / 100
#                 normProb = z / 100
#                 results = manyGames(create(highThresh, highProb, normProb), pr1testing.test11, 10000)
#                 if results[1] > highest['score']:
#                     logging.debug(highest)
#                     highest['score'] = results[1]
#                     highest['highThresh'] = highThresh
#                     highest['highProb'] = highProb
#                     highest['normProb'] = normProb
#     logging.debug(count, 'done. results:', highest)
#     return highest
# 
# pool = Pool()
# results = pool.map(mutateToTenths, [1,2,3,4])
# logging.debug('the verdict is: ', results)

