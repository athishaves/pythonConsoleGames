# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:54:10 2019

@author: Athish
"""
import random

def Roulette():
    
    print("As this is a gamble.., we are not taking your name")
    money = 1000
    print("Your initial amount is : Rs.", money)
    a=1
    
    while(a==1):
        display()
        bettype = int(input("Enter the type of bet "))
        lotval = random.randint(1,36)
        if(money==0):
            a=0
        
        if(bettype==1):
            print()
            print("1 :: bet on red (1-18)")
            print("2 :: bet on green (19-36)")
            b = int(input())
            betamt=int(input("Enter the bet amount "))
            if(betamt>money):
                print("Please bet money less than or equal to", money)
            else:
                money -= betamt
                print("The ball rolled to", lotval)
                if(b==1):
                    if(lotval<19):
                        betamt*=2
                        money+=betamt
                        print("Bet amount got doubled")
                    else:
                        print("You lost the money")
                else:
                    if(lotval>=19):
                        betamt*=2
                        money+=betamt
                        print("Bet amount got doubled")
                    else:
                        print("You lost the money")
                print("Your money value is now Rs.", money)
        
        if(bettype==2):
            print()
            print("1 :: bet on even number")
            print("2 :: bet on odd number")
            b = int(input())
            betamt=int(input("Enter the bet amount "))
            if(betamt>money):
                print("Please bet money less than or equal to", money)
            else:
                money -= betamt
                print("The ball rolled to", lotval)
                if(b==1):
                    if(lotval%2==0):
                        betamt*=2
                        money+=betamt
                        print("Bet amount got doubled")
                    else:
                        print("You lost the money")
                else:
                    if(lotval%2!=0):
                        betamt*=2
                        money+=betamt
                        print("Bet amount got doubled")
                    else:
                        print("You lost the money")
                print("Your money value is now Rs.", money)
        
        if(bettype==3):
            b = int(input("Enter the number you want to bet on (1-36) "))
            betamt=int(input("Enter the bet amount "))
            if(betamt>money):
                print("Please bet money less than or equal to", money)
            else:
                money -= betamt
                print("The ball rolled to", lotval)
                if(lotval==b):
                    betamt*=8
                    money+=betamt
                    print("Bet amount got octopled")
                else:
                    print("You lost the money")
                print("Your money value is now Rs.", money)
                
        a = int(input("Press 1 to continue "))
        
        
    if(money>0):
        print("Thanks for playing")
        print("You are taking Rs.", money, "with you")
    else:
        print("Thanks for playing")
        print("Bring more amount tomorrow ;)")
                    
                
        
        
        
        
def display():
    print("1 :: red (1-18) and green (19-36) bet (2x the bet)")
    print("2 :: odd or even bet (2x the bet)")
    print("3 :: particular number bet (8x the bet)")
    
    
    
    
Roulette()