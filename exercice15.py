'''
Write a function, get_rainfall, that tracks rainfall in a number of cities.
Users of your program will enter the name of a city; if the city name is blank, then the function prints a report before exiting.
'''

def get_rainfall():
  rainfall = {}

  while True:
    city_name = input('Enter a city name : ').lower().strip()

    if not city_name:
      break
    
    else:
      mm_rain = int(input('Enter mm rain : '))
      rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain

  for city, rain in rainfall.items():
    print(f'{city}: {rain}')