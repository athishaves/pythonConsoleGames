# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:35:39 2019

@author: Athish
"""
import random

def HandCricket():
    
    name = input("Enter player's name ")
    
    score=0
    target=random.randint(0,200)
    print("Computer has scored ", target-1, "runs")
    print(name, "!!! Your target is ", target)
    
    while(score<target):
        value = int(input("Enter a number from 1 to 10 : "))
        if(value>10 or value<1):
            print("Enter the correct number")
        else:
            covalue = random.randint(1,10)
            print("Computer says number", covalue)
            if(value==covalue):
                print("You and the computer got the same number")
                print("You got out for", score)
                break
            else:
                score+=value
                print("Your score is now", score)
            
    if(score>=target):
        print()
        print("Congratulations", name ,"!!!! You have won!!!")
    elif(score==target-1):
        print()
        print("Its a draw!!!")
    else:
        print()
        print("Better luck next time!")
        
        
def CrazyCricket():
    
    name = input("Enter player's name ")
    
    score=0
    target=random.randint(0,200)
    print("Computer has scored ", target-1, "runs")
    print(name, "!!! Your target is ", target)
    
    while(score<target):
        value = int(input("Enter a number from 1 to 10 : "))
        if(value>10 or value<1):
            print("Enter the correct number")
        else:
            covalue = random.randint(1,10)
            print("Computer says number", covalue)
            if(value==covalue-1 or value==covalue+1):
                print()
                print("You got out for", score)
                break
            else:
                if(value==covalue):
                    print("Wow!! Your number", value , "is now doubled")
                    value = value**2
                score+=value
                print("Your score is now", score)
            
    if(score>=target):
        print()
        print("Congratulations", name ,"!!!! You have won!!!")
    elif(score==target-1):
        print()
        print("Its a draw!!!")
    else:
        print("Better luck next time!")