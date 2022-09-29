# GAME OF NIM
# Qianhui Vanessa Zou
# CSCI 77800 Fall 2022
# collaborators:
# consulted: Geeks for Geeks, thinkcspy, codecademy

"""
The Rules of Life:
   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.
   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.
   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.
   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.

"""
import random as r

ALIVE = 'X'
DEAD = 'O'

# create, initialize, and return empty board (all cells dead)
def createNewBoard(rows, cols):
  board = []
  
  for i in range(rows):
    row = []
    
    for j in range(cols):
    
return board
