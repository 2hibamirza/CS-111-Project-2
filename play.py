# Project 2 - Spelling Bee 2.0, play.py (file 2 of 3)
# Spelling Bee Game
# Hiba Mirza
# CS 111, Fall 2022, Reckinger
# Creates a game in which users need to guess as many possible words with 7 letters
# prompts user for word that solves the puzzle

global letters, dictionary, word, score, words_list, scores_list # do not change or add to

word = str(input("Word: "))
word_lower = word.lower()


if (word_lower in dictionary):
  if (len(word) >= 4):
    score = dictionary[word_lower]
    print("Score for " + word + ":", int(score))
    scores_list.append(score)
    words_list.append(word)
    if (letters[0].lower() not in word.lower()):
      print(word + " does not contain the middle letter, " + letters[0] + " so no points given.")
  if(len(word) < 4):
    print("Score for " + word + ": 0")
    print(word + " contains less than 4 letters so no points given.")
    score = 0
    words_list.append(word)
    scores_list.append(score)
    if (letters[0].lower() not in word.lower()):
      print(word + " does not contain the middle letter, " + letters[0] + " so no points given.")
elif (word not in dictionary):
  score = 0
  words_list.append(word)
  scores_list.append(score)
  # output score
  print("Score for " + word + ":", int(score))
  print(word + " is not in the dictionary so no points given.")
else:
  score = 0
  words_list.append(word)
  scores_list.append(score)
  # output score
  print("Score for " + word + ": 0")