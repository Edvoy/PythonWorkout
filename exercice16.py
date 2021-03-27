'''
Write a function, dictdiff, that takes two dicts as arguments.
The function returns a new dict that expresses the difference between the two dicts.
If there are no differences between the dicts, dictdiff returns an empty dict.
For each key-value pair that differs, the return value of dictdiff will have a key-value pair in which the value is a list containing the values from the two different dicts.
'''

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'e':4}


def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()
    
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key),second.get(key)]
   
    return output