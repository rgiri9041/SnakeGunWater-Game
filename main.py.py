# WAP to make a game of gun water and snake
'''
Docstring for project.main.py

-1 = snake
0 = gun 
1 = water
'''


import random
comp = random.randint(-1,1)
youstr = input("Enter you choice (Gun, Water, Snake): ")
youDict = {"g": 0, "w": 1, "s": -1}
you = youDict[youstr]

if(comp == you):
    print("Match Draw, Try Again!!")

elif((comp == -1 and you == 0) or (comp == 0 and you == 1) or (comp == 1 and you == -1)):
    print("You Win")

else:
    print("Sorry. You Lose")