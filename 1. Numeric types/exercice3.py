'''
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until the user presses Enter.
At that point, the function exits—but only after calculating and displaying the average time that the 10 km runs took.
'''

def run_timing():
 
  count = 0
  total_runtime = 0
 
  while True :
    runtime = int(input('How long did it take you to run 10km? '))
    if not runtime:
     break
    total_runtime += runtime
    count += 1
    print(runtime)

  run_average = total_runtime/count
  print(run_average)

'''
SOLUTION:

def run_timing():
  
  """ Asks the user repeatedly for numeric input. Prints the average time and number of runs."""
 
  number_of_runs = 0
  total_time = 0

  while True:
    one_run = input('Enter 10 km run time: ')
    if not one_run:
      break

    number_of_runs += 1
    total_time += float(one_run)
 
  average_time = total_time / number_of_runs
  print(f'Average of {average_time}, over {number_of_runs} runs')
'''