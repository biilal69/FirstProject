# File: CS112_A1_T2_3_Yousefbilal.py
# Purpose: This is a 2-player game called subtract a square. The players decide on wether to generate a random number
# of coins, or set a number on their own. Each player gets a turn to subtract a square number from the pile.
# The player that subtracts the last number, is the winner.
# Author: Yousef Bilal
# ID: 20231224

# Imports
import random

# Instructions
print("Game name: Subtract a square")
print("In this game, each player will subtract a perfect square root number from a random pile or entered number.")
print("the player that will subtract the last number, making the result is 0, will win.")
print("Rules: players will only subtract perfect square root numbers, e.g: 1, 4, 9, etc...")
print("Shall we play?")

# Players names
player1 = str(input("Player 1: "))
player2 = str(input("Player 2: "))

# Options
while True:
    print("\n")
    print("A: Random pile size")
    print("B: Enter desired pile size")
    choice = input("Enter your choice: ").upper()
    if choice == "A":
        pile_size = random.randint(10, 1000)
        print("The pile size is", pile_size)
        break
    elif choice == "B":
        pile_size = int(input("Enter desired pile size: "))
        break
    else:
        print("Please select a valid choice!")

while pile_size > 0:
    # Player 1
    while True:
        move = int(input(f"{player1} enter a number: "))
        sqrt_move = move ** 0.5
        if move <= 0:
            print("Please enter a number greater than zero.")
            continue
        elif move > pile_size:
            print("Please enter a number less than the pile size!")
            continue
        if not sqrt_move.is_integer():
            print("Please enter a valid square number!")
            continue
        pile_size = pile_size - move
        if pile_size == 0:
            print(f"{player1} is the winner!")
            break
        else:
            print("Current pile size is", pile_size)
            break
    if pile_size == 0:
        break
    else:
        # Player 2
        while True:
            move = int(input(f"{player2} enter a number: "))
            sqrt_move = move ** 0.5
            if move <= 0:
                print("Please enter a number greater than zero.")
                continue
            elif move > pile_size:
                print("Please enter a number less than the pile size!")
                continue
            if not sqrt_move.is_integer():
                print("Please enter a valid square number!")
                continue
            pile_size = pile_size - move
            if pile_size == 0:
                print(f"{player2} is the winner!")
                break
            else:
                print("Current pile size is", pile_size)
                break
