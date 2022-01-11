'''
Author: Adityaraj Yadav 
Date: 10 January 2022
Project Name: Guess With Friend
Purpose:For Practising Purpose
'''

import random
Player_1_num = int(input("\nEnter the number from where you have to guess: "))
Player_2_num = int(input("Enter the number where you have to stop the guess: "))
rand_num = random.randint(Player_1_num,Player_2_num)
rand_num2 = random.randint(Player_1_num,Player_2_num)
Time_Count = 0
def play_1():
    Time_Count = 0
    while True:
        Time_Count += 1
        with open("Player_1.txt","w") as f:
            f.write(f"{Time_Count}")
        Player_1 = int(input("\nFriend Turn: Enter the number: "))
        if Player_1 == rand_num:
            print("Congraculations! You guess the correct number")
        elif Player_1 > rand_num:
            print("Enter Smaller Number and try again")
        elif Player_1 < rand_num:
            print("Enter Larger Number and try again")

def play_2():
    Time_Count2 = 0
    while True:
        Time_Count2 += 1
        with open("Player_2.txt","w") as f:
            f.write(f"{Time_Count2}")
        Player_2 = int(input("\nYour Turn: Enter the number: "))
        if Player_2 == rand_num2:
            print("Congraculations! You guess the correct number")
        elif Player_2 > rand_num2:
            print("Enter Smaller Number and try again")
        elif Player_2 < rand_num2:
            print("Enter Larger Number and try again")
def Win():    
    if Time_Count > Time_Count2:
        print("You win!")
    elif Time_Count < Time_Count2:
        print("You Loose!")
rand = random.randint(1, 2)
if rand == 1:
    play_1()
    play_2()
    exit()
elif rand == 2:
    play_2()
    play_1()
    exit()
Win()
# while True:
#     Time_Count += 1
#     with open("Player_1.txt","w") as f:
#         f.write(f"{Time_Count}")
#     Player_1 = int(input("\nFriend Turn: Enter the number: "))
#     if Player_1 == rand_num:
#         print("Congraculations! You guess the correct number")
#         # break
#         exit()
#     elif Player_1 > rand_num:
#         print("Enter Smaller Number and try again")
#     elif Player_1 < rand_num:
#         print("Enter Larger Number and try again")

# while True:
#     Time_Count2 += 1
#     with open("Player_2.txt","w") as f:
#         f.write(f"{Time_Count2}")
#     Player_2 = int(input("\nYour Turn: Enter the number: "))
#     if Player_2 == rand_num2:
#         print("Congraculations! You guess the correct number")
#         if Time_Count > Time_Count2:
#             print("You win!")
#         elif Time_Count < Time_Count2:
#             print("You Loose!")
#         # break
#         exit()
#     elif Player_2 > rand_num2:
#         print("Enter Smaller Number and try again")
#     elif Player_2 < rand_num2:
#         print("Enter Larger Number and try again")