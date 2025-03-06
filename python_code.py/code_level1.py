# Asking for us to write code that will return all the open tables at a restaurant
# We need to use a function to store code
# A for loop to loop thorugh all of the tables and find the empty ones.
# A if so we can return the right open table marked 'o'
# A print and return so we can run the code.
def get_open_tables(restaurant_tables, timeslot):
 
  open_tables = []
  for i in range(1, len(restaurant_tables[0])):  
    if restaurant_tables[timeslot][i] == 'o':
      open_tables.append(restaurant_tables[0][i])  
  return open_tables

restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]


timeslot_to_check = 2

free_tables_at_timeslot = get_open_tables(restaurant_tables, timeslot_to_check)
print(f"Free tables at timeslot {timeslot_to_check}: {free_tables_at_timeslot}")