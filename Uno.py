# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 00:10:41 2019

@author: Athish
"""

import random

def Uno():
    
    player1 = input("Enter your name ")
    set1 = ['R', 'B', 'Y', 'G']
    set2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    set = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10']
    carda = random.choice(set1)
    cardb = random.choice(set2)
    card = carda + cardb
    print("The initial card =", card)
    for i in range (len(set)):
        if(set[i]==card):
            index = i
    del set[index]
    c=[]
    ca=[]
    cb=[]
    cc=[]
    cac=[]
    cbc=[]
    for i in range (0,3):
        card1a = random.choice(set1)            
        card1b = random.choice(set2)
        card1=(card1a + card1b)
        while(card1 not in set):
            card1a = random.choice(set1)            
            card1b = random.choice(set2)
            card1=(card1a + card1b)
        ca.append(card1a)
        cb.append(card1b)
        c.append(card1)
        for i in range (len(set)):
            if(set[i]==card1):
                index = i
        del set[index]
        card1ac = random.choice(set1)            
        card1bc = random.choice(set2)
        card1c=(card1ac + card1bc)
        while(card1c not in set):
            card1ac = random.choice(set1)            
            card1bc = random.choice(set2)
            card1c=(card1ac + card1bc)
        cac.append(card1ac)
        cbc.append(card1bc)
        cc.append(card1c)
        for i in range (len(set)):
            if(set[i]==card1c):
                index = i
        del set[index]
    print("Your cards are", *c)
    print(*cc)
        
    while(len(c)!=0 or len(cc)!=0 or len(set)!=0):
        if(len(c)==0 or len(cc)==0 or len(set)==0):
            break
        num = int(input("0::Drop a card....1::Pick a card "))
        if(num==1):
            card1a = random.choice(set1)            
            card1b = random.choice(set2)
            card1=(card1a + card1b)
            while(card1 not in set):
                card1a = random.choice(set1)            
                card1b = random.choice(set2)
                card1=(card1a + card1b)
            ca.append(card1a)
            cb.append(card1b)
            c.append(card1)
            for i in range (len(set)):
                if(set[i]==card1):
                    index = i
            del set[index]
            if(card1a==carda or card1b==cardb):
                carda=card1a
                cardb=card1b
                card=carda+cardb
                del ca[len(c)-1]
                del cb[len(c)-1]
                del c[len(c)-1]
                print("You picked and eliminated", card)
            print(*c)
            print("The card on the top is =", card)
        if(num==0):
            drop = int(input("Enter the card to be eliminated "))
            if(ca[drop-1]!=carda and cb[drop-1]!=cardb):
                card=ca[drop-1]+cb[drop-1]
                print(card,"cannot be deleted")
                print("Enter the valid card")
                print("Sorry your turn's over")
            else:
                carda = ca[drop-1]
                cardb = cb[drop-1]
                card = carda + cardb
                del ca[drop-1]
                del cb[drop-1]
                del c[drop-1]
                print(*c)
                print("The card on the top is =", card)
        if(len(c)==0 or len(set)==0):
            break
        else:
            some = len(cc)
            for z in range (len(cc)):
                if(cac[z]==carda or cbc[z]==cardb):
                    carda=cac[z]
                    cardb=cbc[z]
                    card=carda+cardb
                    del cac[z]
                    del cbc[z]
                    del cc[z]
                    print(*cc)
                    print("Computer eliminated", card)
                    print("The card on the top is =", card)
                    break
            if(some==len(cc)):
                card1ac = random.choice(set1)            
                card1bc = random.choice(set2)
                card1c=(card1ac + card1bc)
                while(card1c not in set):
                    card1ac = random.choice(set1)            
                    card1bc = random.choice(set2)
                    card1c=(card1ac + card1bc)
                cac.append(card1ac)
                cbc.append(card1bc)
                cc.append(card1c)
                for i in range (len(set)):
                    if(set[i]==card1c):
                        index = i
                del set[index]
                print("Computer picked a card")
                if(card1ac==carda or card1bc==cardb):
                    carda=card1ac
                    cardb=card1bc
                    card=carda+cardb
                    del cac[len(cc)-1]
                    del cbc[len(cc)-1]
                    del cc[len(cc)-1]
                    print(*cc)
                    print("Computer eliminated", card)
                    print("The card on the top is =", card)
                else:
                    print("The card on the top is still =", card)
                print(*cc)
        
    if(len(c)==0):
        print("Congratulations!!!",player1,"You have won")
    elif(len(set)==0 and len(cc)!=0):
        print("Its a draw")
    else:
        print("You couldn't even win against a machine... You are such a loser!!!",player1)
            
            
        
Uno()