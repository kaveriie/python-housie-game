#1-100 random numbers take 10 nos.(they shouldnt repeat) give 5 to one player and remaining 5 to other
import os


msg="WELCOME TO HOUSIE GAME"
print(msg.center(100))
print("\t\t\t\t====================================")

import random
list=[]                 #empty list
for i in range(100):             #generating 10 random numbers
    r=random.randint(1,100)         #range btwn 1 to 100
    if r not in list:
        list.append(r)              #to make sure there are no duplicates
    if len(list) == 12:
        break
#print(list)


player1= list[:6]
print("Player 1: You have the following numbers:",end="\t")
for i in player1:
    print(i, end=" | ")

player2= list[6:]
print("\nPlayer 2: You have the following numbers:",end="\t")
for i in player2:
    print(i, end=" | ")



def check(p,n):
    #p=player
    if p == []:
        print("\n*********************** WINNER : PLAYER",n,"***********************")
        exit()
    else:
        pass



drawn=[]
for i in range(100):
    drawn_number=random.choice(list)
    #print(drawn_number)


    if drawn_number in drawn:
        #print("Passing it")
        pass
    else:
        drawn.append(drawn_number)
        input("\nPress enter to draw a number:")
        print("\n\n*** Number Drawn:",drawn_number,"***")        
    #print("current drawn=",drawn)



    if drawn_number in player1:
        player1.remove(drawn_number)
        print("Player 1:")
        for i in player1:
            print(i,end=" | ")
        print("\n")
        print("Player 2:")
        for i in player2:
            print(i,end=" | ")

        check(player1,1)

    elif drawn_number in player2:
        player2.remove(drawn_number)
        print("Player 1:")
        for i in player1:
            print(i,end=" | ")
        print("\n")
        print("Player 2:")
        for i in player2:
            print(i,end=" | ")
        check(player2,2)
    else:
        pass



input()
os.system("pause")