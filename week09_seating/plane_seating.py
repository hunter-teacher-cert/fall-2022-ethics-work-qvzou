# Looked up online for seating coding due to complexity of coding.  This code was cited from another repository since we were unable to fully implement our recommended equity strategies, which included Delta's dynamic seating algorithm, seating for people with disability, seating for social distancing for people with anxiety since thepandemic.  However, this code does address groups with children, which was one of our equity issues and that's why we used this code. 

# Here is the link to the repository code https://github.com/hunter-teacher-cert/fall-2020-ethics-work-JimmyDillon-CS/blob/master/05-seatr/seat_algorithm-2.py

# Here  is the link to the article about 
# Delta's Dynamic Seating Algorithm that we tried to implement
# https://www.travelinglifestyle.net/deltas-new-seat-algorithm-makes-it-easier-for-family-members-to-sit-together/

############### Library Imports ###############
import math
import random
import copy

############### Global Variables ###############
seat_map = [] # two-dimensional array to hold seat information
seat_list = dict() # a map of passenger names and seat locations
waitlist = [] # holds Party elements
max_seats = 180 # maximum number of seats on the plane
seats_filled = 0 # increases as seats are filled

############### Class Definitions ###############

# The class Party holds information about non-seat-choosers:
# size of the party
# includes child/children?
# Parties will be added to a list called waitlist
class Party:

  def __init__(self, members, size, has_child):
    self.members = members
    self.size = size
    self.has_child = has_child

  def __str__(self):
    return "Members: % s size: % s has_child: % s" % (self.members, self.size, self.has_child)  

############### Methods ###############

# User Interface:
# Asks the user if they are picking a seat or not
# Calls seat_chooser() if yes
# Calls concierge() if no
# Exits when plane is fully booked
def user_prompt():
  return

# Creates a new seat map (30x6)
#   ABC DEF
#01 OOO OOO
#02 OOO OOO
#03 OOO OOO
#04 OOO OOO
#05 OOO OOO
#06 OOO OOO
#07 OOO OOO
#08 OOO OOO
#09 OOO OOO
#10 OOO OOO

def create_map():
  empty_row = [False, False, False, False, False, False]
  for x in range(30):
    seat_map.append(empty_row.copy())
  return

# Prints/displays seat map with open (o) and closed (x) seats
def display_map():
  print ("   ABC DEF") #display header of seat letters
  for x in range(30):
    if x < 10:
      print ("0", end = '') #formatting
    print (str(x) + " ", end = '') #row numbers
    for y in range(6):
      if seat_map[x][y] == False:
        print("O", end = '')
      else:
        print("X", end = '')
      if y == 2:
        print(" ", end = '') #print aisle
    print("")

  return

# Updates the map with x and seat_list
def reserve_seat(seat, name):
  row = int(seat[0:2]) # Grab and cast row number
  # print(row)
  seat_num = ord(seat[-1])-65 # Converts seat letter to ascii then translates
  #print(seat)

  if seat_map[row][seat_num] == True:
    print("seat is already full, please choose another seat")
    display_map()
  else: 
    seat_map[row][seat_num] = True
    print("You reserved the seat!")
    seat_list[seat]=name

  return

# Handles seat choice, calls display_map(), reserve_seat()
def seat_chooser():
  return

create_map()
display_map()

# Creates a party based on user information and places them on the waitlist
def concierge(members, has_child):
  tmp = Party (members, len(members), has_child)
  waitlist.append(copy.deepcopy(tmp))
  return

# Sorts waitlist to prioritize groups with children
def sort_waitlist():
  w_child = []
  wo_child = []
  for x in waitlist:
    if x.has_child == True:
      w_child.append(x)
    else:
      wo_child.append(x)
  
  waitlist.clear()
  # Sort the w_child list by party size
  for i in range(len(w_child)): 
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(w_child)): 
        if w_child[min_idx].size > w_child[j].size: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    w_child[i], w_child[min_idx] = w_child[min_idx], w_child[i]
  
    # Sort the wo_child list by party size
  for i in range(len(wo_child)): 
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(wo_child)): 
        if wo_child[min_idx].size > wo_child[j].size: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    wo_child[i], wo_child[min_idx] = wo_child[min_idx], wo_child[i] 


# Finds maximum open clusters of seats based on a specific size
def find_max_open_seats():
  max_open_seats = 0
  open_seats = 0
  for x in range(30):
    for y in range(6):
      if seat_map[x][y] == False:
        open_seats += 1
      else:
        if open_seats > max_open_seats:
          max_open_seats = open_seats
        open_seats = 0
      if open_seats > max_open_seats:
        max_open_seats = open_seats
      open_seats = 0
  return max_open_seats

# Seats parties from the waitlist
# Removes that party from the waitlist
def seat_party ():
  return

#create_map()
#reserve_seat("00A", "Jimmy Dillon")
#reserve_seat("02A", "Jimmy Dillon")
#reserve_seat("01A", "Hiral Dillon")
#p = Party(["peter", "paul", "mary"], 3, True)
#concierge(["john", "paul", "ringo", "george"], False)
#print(p)
#print(waitlist)
#print(seat_list)
#display_map()