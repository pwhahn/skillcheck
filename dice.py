import random

"""    My interest in role-playing games, specifically of the Old School
Renaissance (OSR) style, have really piqued my interest in developing my
own system. I would like to create a skill check system that is easy and
also has some realism. This program calculates the number of times dice
are rolled to level up from a starting level to an ending level. The
program allows you to change the number of dice being rolled, the number
of sides on the dice, the starting and ending levels, and the number of
game simulations to run.   """

#Modify number of DICE and SIDES of dice.
def roll(dice = 2, sides = 6):
    result = 0
    for _ in range(dice):
        result += random.randint(1, sides)
    return result

#Modify START and END levels.
def skills(start = 4, end = 12):
    level = start
    check = 0 #Counts successful roll checks.
    turn = 0 #Counts number of times the dice are rolled.
    
    while True:
        result = roll()
        turn += 1
        if result <= level: #Condition for successful roll check.
            check += 1
            #print(turn, level, result, check, "Skill Check PASS")
            if check == level: #Condition to increase level.
                result = roll()
                turn += 1
                check = 0
                if result > level:
                    #print(turn, level, result, check, "---- Level Check PASS")
                    level += 1
                #else:
                    #print(turn, level, result, check, "---- Level Check FAIL")
                check = 0
                if level == end: #Condition to stop the game.
                    break
        #else:
            #print(turn, level, result, check, "Skill Check FAIL")
    print("Dice Rolls to Level Up:", turn, "Ending Level:", level)

#Modify number of GAME simulations to run.
def games(game = 10):
    for _ in range(game):
        skills()

games()
