'''
For this exercise
Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following: Too high - Too low - Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.
'''
import random as rand

def guessing_game():
  random_number = rand.randint(0,100)
  user_number = int(input('Guess the number between 0 and 100 : '))
  
  while user_number != random_number:
   
    if random_number > user_number:
      print('Too low')
      user_number = int(input('Try again : '))
  
    elif random_number < user_number:
      print('Too high')
      user_number = int(input('Try again : '))
 
  print('Just right')