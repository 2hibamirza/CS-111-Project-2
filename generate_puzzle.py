# Project 2 - Spelling Bee 2.0, generate_puzzle.py (file 1 of 3)
# Spelling Bee Game
# Hiba Mirza
# CS 111, Fall 2022, Reckinger
# Creates a game in which users need to guess as many possible words with 7 letters
# prompts user for word that solves the puzzle

global letters, valid # do not change or add to

# prompt user to enter 7 letters
letters = input("Enter 7 puzzle letters: ")

# user input is (changed to) all uppercase letters
letters = letters.upper()
letters_set = set(letters)

if (len(letters) == 7):
  if len(letters_set) == len(letters):
    if (letters.isalpha()):
      valid = True
      print("--------SPELLING BEE-------")
      print("--------- / ¯¯¯ \ ---------")
      print("---------    " + letters[2] + "    ---------")
      print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
      print("----   " + letters[3] + "           " + letters[1] + "   ----")
      print("----\ ___ / ¯¯¯ \ ___ /----")
      print("---------    " + letters[0] + "    ---------")
      print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
      print("----   " + letters[4] + "           " + letters[6] + "   ----")
      print("----\ ___ / ¯¯¯ \ ___ /----")
      print("---------    " + letters[5] + "    ---------")
      print("--------- \ ___ / ---------")
    else:
      valid = False
      print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
  else:
    valid = False
    print("Invalid puzzle, must enter 7 unique letters.")
else:
  valid = False
  print("Invalid puzzle, must enter exactly 7 letters.")