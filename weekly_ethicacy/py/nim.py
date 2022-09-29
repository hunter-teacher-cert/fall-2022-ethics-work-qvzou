# GAME OF NIM
# Qianhui Vanessa Zou
# CSCI 77800 Fall 2022
# collaborators:
# consulted: Brother in law who works at Google, thinkcspy, codecademy, nim java code

import random

stones = 12
stonesTaken = int()
playing = True

print(
    "Let's play the game of Nim.  There is a bag with 12 stones.  Your goal is to take the last one."
)

while (playing):
    print("There are %s stones remaining!" %stones)
    stonesTaken = input("How many stones do you wish to take?  Pick 1-3:  ")
    stonesTaken = int(stonesTaken)
    if stonesTaken > 0 and stonesTaken <= 3 and stonesTaken <= stones:
        stones -= stonesTaken
    else:
        print("Invalid move. Try again")
        continue

    if stones == 0:
        print("You win!")
        playing = False;
        break

    if stones % 4 == 1:
        stonesTaken = 1
    elif stones % 4 == 2:
        stonesTaken = 2
    elif stones % 4 == 3:
        stonesTaken = 3
    else:
        stonesTaken = 1

    print("AI takes %s stones " % stonesTaken)
    stones -= stonesTaken

    if stones == 0:
        print("AI wins!")
        playing = False

print("Game Over!")