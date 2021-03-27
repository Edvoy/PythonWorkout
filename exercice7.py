'''
For this exercise, you’ll write a function (called ubbi_dubbi) that takes a single word (string) as an argument.
It returns a string, the word’s translation into Ubbi Dubb
In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub.
Thus milk becomes mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am).
In theory, you only put an ub before every vowel sound, rather than before each vowel.
Given that this is a book about Python and not linguistics, I hope that you’ll forgive this slight dif- ference in definition.
'''

def ubbi_dubbi(word):
  ubbi_translation = ""
  for n in range(len(word)):
    if word[n] in 'aeiou':
      ubbi_translation += "ub"+word[n]
    else:
      ubbi_translation += word[n]
  print(ubbi_translation)