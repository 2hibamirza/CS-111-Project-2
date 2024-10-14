# Project 2 - Spelling Bee 2.0, play.py (file 2 of 3)
# Spelling Bee Game
# Hiba Mirza
# CS 111, Fall 2022, Reckinger
# Creates a game in which users need to guess as many possible words with 7 letters
# prompts user for word that solves the puzzle

global name, words_list, scores_list, bonus # do not change or add to

# creates name variable
name = str(name)

# output
print("************************")
print("GAME OVER")
print("************************")

if (0 in scores_list):
  print("You lost, " + name + "!")
else:
  print("You win, " + name + "!")

# outputs sum of all scores
print("Final Score:", sum(scores_list))

# output 6 words along with scores for each word
print("Words played:")
print(words_list[0] + '(' + str(scores_list[0]) + ')')
print(words_list[1] + '(' + str(scores_list[1]) + ')')
print(words_list[2] + '(' + str(scores_list[2]) + ')')
print(words_list[3] + '(' + str(scores_list[3]) + ')')
print(words_list[4] + '(' + str(scores_list[4]) + ')')
print(words_list[5] + '(' + str(scores_list[5]) + ')')

if bonus == True:
  print("Congrats on finding a bonus word!")