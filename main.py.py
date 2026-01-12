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
reverseDict = {0: "Gun", 1: "Water", -1: "Snake"}
you = youDict[youstr]
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[comp]}")

if(comp == you):
    print("Match Draw, Try Again!!")

elif((comp == -1 and you == 0) or (comp == 0 and you == 1) or (comp == 1 and you == -1)):
    print("You Win")
elif((you == -1 and comp == 0) or (you == 0 and comp == 1) or (you == 1 and comp == -1)):
    print("Sorry You lose (:)")
else:
    print("Something went wrong")