'''
In this exercise, you’ll explore this idea by writing a function, strsort,
that takes a single string as its input and returns a string.
The returned string should contain the same characters as the input,
except that its characters should be sorted in order, from the lowest Unicode value to the highest Unicode value.
For example, the result of invoking strsort('cba') will be the string abc.
'''

def strsort(string):
  sorted_str = ""
  for l in range(len(string)):
    if string[l]>sorted_str[len(sorted_str)-1:]:
      sorted_str += string[l]
    else:
      sorted_str = string[l] + sorted_str
  print(sorted_str)

''' solution
def strsort(a_string):
    return ''.join(sorted(a_string))
print(strsort('cbjeaf'))
'''