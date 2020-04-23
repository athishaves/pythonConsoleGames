# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:17:54 2020

@author: athis
"""

# a - Athish
# b - Computer

import random

numbers = 4

print("Here is an easy game you are going to play against the computer")
print("Just guess ", numbers, " numbers.  Range (1-10)")
print("At each round, guess a number which the computer has guessed")
print("And in the same way, the computer is also going to guess your number if its true say T and if false, say false")
print("Who guesses all the numbers the other person has guessed is going to win!")
print("So lets see who is going to win, You or THE COMPUTER")
print("")

a = []

rand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for _ in range (numbers):
    num = random.choice(rand)
    b.append(num)
    rand.remove(num)
# print("B = ", b)
print("The computer has finished guessing the number")
    
rand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
scoreA = 0
scoreB = 0

chance = 0

while(scoreA<numbers and scoreB<numbers):
    
    if(chance==0):
        # A should guess the number
        numberA = int(input("Guess the computer's number "))
        # Checking the guessed number is correct or not
        guessed = False
        for i in b:
            if i==numberA:
                guessed = True
                break;
        if (guessed):
            print("You have guessed correct")
            scoreA += 1
            b.remove(numberA)
        else:
            print("Your guess in wrong")
        chance = 1
                
    else:
        # Computer's chance
        numberB = random.choice(rand)
        print("The computer has guessed " , numberB , " Is that right?")
        judge = input("Enter T if true and F if false (case sensitive) ")
        if(judge=="T" or judge=="t"):
            print("The computer has guessed correctly")
            scoreB += 1
        else:
            print("The computer has guessed wrong")
        rand.remove(numberB)
        chance = 0
        
    # print("Rand = ", rand)        
    print("Your Score " , scoreA)
    print("Computer's Score " , scoreB)
    print("")
    
if(scoreA==4):
    print("Congratulations! You won")
else:
    print("Lol! You couldn't win even against a Machine!!")
    print("What a looser")