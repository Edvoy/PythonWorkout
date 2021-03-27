'''
In this exercise, I want you to create a new constant dict, called MENU, representing the possible items you can order at a restaurant. The keys will be strings, and the val- ues will be prices (i.e., integers). You should then write a function, restaurant, that asks the user to enter an order:
If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks the user again for their order.
If the user enters the name of a dish not on the menu, the program scolds the user (mildly). It then asks the user again for their order.
If the user enters an empty string, the program stops prompting and prints the total amount.
'''

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
  total = 0
  while True:
    order = input('Order :')
    if not order:
      break
    if order in MENU:
      price = MENU[order]
      total += MENU[order]
      print(f'{order} costs {price}$, total is {total}$')
    else:
      print(f'sorry, go search {order} yourself !')
      
  print(f'Your total order is {total}$')