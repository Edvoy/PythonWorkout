'''
Let’s assume you have phone book data in a list of dicts, as follows:
PEOPLE = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'}, {'first':'Donald', 'last':'Trump'], 'email':'president@whitehouse.gov'}, {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}]
Write a function, alphabetize_names, that assumes the existence of a PEOPLE constant defined as shown in the code. The function should return the list of dicts, but sorted by last name and then by first name.
'''

import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts,
        key=operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))