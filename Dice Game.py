# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:49:29 2019

@author: Athish
"""
import random

def SnakeAndLadder():
    
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    print()
    
    score1 = 0
    score2 = 0
    
    while(score1<100 and score2<100):
        print("It's ", player1 ,"'s turn")
        value1 = random.randint(1,6)
        if((score1+value1)<=100):
            score1 += value1
            score1 = Snakes(score1)
            score1 = Ladder(score1)
        print("You have got ", value1)
        print("Your score is now", score1)
        input()
        
        if(score1<100):
            print("It's ", player2 ,"'s turn")
            value2 = random.randint(1,6)
            if((score2+value2)<=100):
                score2 += value2
                score2 = Snakes(score2)
                score2 = Ladder(score2)
            print("You have got ", value2)  
            print("Your score is now", score2)
            input()
            
    if(score1==100):
        print("Congratulations!!! ", player1 ,"has won!!!")
        print("Thanks for playing")
    if(score2==100):
        print("Congratulations!!! ", player2 ,"has won!!!")
        print("Thanks for playing")
        
        
def Snakes(n):
    if(n==32):
        print("You dropped down from 32 to 6 with a snake bite")
        return(6)
    elif(n==74):
        print("You dropped down from 74 to 22 with a snake bite")
        return(22)
    elif(n==86):
        print("You dropped down from 86 to 51 with a snake bite")
        return(51)
    elif(n==99):
        print("You dropped down from 99 to 39 with a snake bite")
        return(39)
    else:
        return(n)
        
def Ladder(n):
    if(n==9):
        print("You jumped from 9 to 31 with a ladder")
        return(31)
    elif(n==16):
        print("You jumped from 16 to 45 with a ladder")
        return(45)
    elif(n==18):
        print("You jumped from 18 to 64 with a ladder")
        return(64)
    elif(n==48):
        print("You jumped from 48 to 66 with a ladder")
        return(66)
    elif(n==50):
        print("You jumped from 50 to 93 with a ladder")
        return(93)
    elif(n==63):
        print("You jumped from 63 to 81 with a ladder")
        return(81)
    else:
        return(n)