'''
The rules for translating words from English into Pig Latin are quite simple:
If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word.
So “air” becomes “airway” and “eat” becomes “eatway.”
If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add “ay.”
Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”
For this exercise, write a Python function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin. You may assume that the word contains no capital letters or punctuation.
'''

def pig_latin():
  
  en_word = input('Enter an english word : ')
  vowel = ["a","e","i","o","u"]
  pig_word = ""

  if en_word[0] in vowel : 
    pig_word = en_word+'way'
  
  else :
    pig_word = en_word[1:]+ en_word[0] +'ay'

  print(pig_word)

'''
SOLUTION

  def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
'''