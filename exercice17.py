'''
In this exercise, you can assume that your Python program contains a list of integers.
We want to print the number of different integers contained within that list.
'''

def how_many_different_numbers(numbers):
  unique_numbers = set(numbers)
  return len(unique_numbers), unique_numbers