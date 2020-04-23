# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:10:07 2019

@author: Athish
"""
import random

def AndBahar():
    
    print("As this a gambling game, we are not taking your name")
    print("Thank me later ;)")
    print()
    print("S :: Spades")    
    print("H :: Hearts")    
    print("D :: Diamond")    
    print("C :: Clubs") 
    money = 1000
    print("You have given Rs.",money,"at the first")
    z=1
    while(z==1):
        bet = int(input("Place your bet (1::Andar.....2::Bahar) "))
        betamt = int(input("Enter bet amount "))
        if(betamt>money):
            print("Enter the money less than or equal to",money)
        else:
            money-=betamt
            pack1=['S', 'H', 'D', 'C']
            pack2 = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            carda = random.choice(pack1)
            cardb = random.choice(pack2)
            card = carda + cardb
            print()
            print("The initial card is", card)
            cards = ['SA', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'HA', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'DA', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'CA', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']
            for i in range (len(cards)):
                if(cards[i]==card):
                    index = i
            del cards[index]
            a=1
            while(a==1):
                input()
                print("Andar")
                card1a = random.choice(pack1)
                card1b = random.choice(pack2)
                card1 = card1a + card1b
                while(card1 not in cards):
                    card1a = random.choice(pack1)
                    card1b = random.choice(pack2)
                    card1 = card1a + card1b
                print(card1)
                for i in range (len(cards)):
                    if(cards[i]==card1):
                        index = i
                del cards[index]
                if(card1b!=cardb):
                    input()
                    print("Bahar")
                    card2a = random.choice(pack1)
                    card2b = random.choice(pack2)
                    card2 = card2a + card2b
                    while(card2 not in cards):
                        card2a = random.choice(pack1)
                        card2b = random.choice(pack2)
                        card2 = card2a + card2b    
                    print(card2)
                    for i in range (len(cards)):
                        if(cards[i]==card2):
                            index = i
                    del cards[index]
                    if(card2b==cardb):
                        a=0
                else:
                    a=0
        if(card1b==cardb):
            if(bet==1):
                print("Your money got doubled")
                money += 2*betamt
            else:
                print("You lost the match")
        if(card2b==cardb):
            if(bet==2):
                print("Your money got doubled")
                money += 2*betamt
            else:
                print("You lost the match")
        
        print("Your money is now", money)
        z=int(input("1::Continue.....0:Exit "))
    print("You took Rs.", money, "with you")
    print("Thanks for playing")
    
AndBahar()