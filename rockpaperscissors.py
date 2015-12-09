import time
import random

b = ["rock", "paper", "scissors"]
c = random.choice(b)

print("enter rock, paper or scissors")
a = input()
time.sleep(1)
if a == c:
    print ("it was a draw!")

def go():
    time.sleep(1)
    print ("the computer chose " + c)

    

##  if          a is ROCK
if a == b[0]:
## c is paper and a is rock
##                              paper wins
    if c == b[1]:
        print("the computer won!")
        go()

## c is sicssors and a is rock
##                              rock wins
    if c == b[2]:
        print("you won!")
        go()

## if       a is PAPER
if a == b[1]:

##   if a is paper and c is  rock
    if c == b[0]:
        print("you won!")
        go()

    if c == b[2]:
        print("the computer won!")
        go()

## if     a is SCISSORS
if a == b[2]:

##    is a is scissors and c is rock

    if c == b[0]:
        print("the computer won!")
        go()

    if c == b [1]:
        print("you won!")
        go()



        
        
