# Asking for us to write code that will return all the open tables at a restaurant
# We need to use a function to store code
# A for loop to loop thorugh all of the tables and find the empty ones.
# A if so we can return the right open table marked 'o'
# A print and return so we can run the code.
# For level 2 the goal is to find one table that can sit a certain amount of people.
# Add the second function to store code.
# Another for loop, if, and print.

def get_open_tables(restaurant_schedule, time_slot):
    available_tables = []  
   
    for col in range(1, len(restaurant_schedule[0])):  
        if restaurant_schedule[time_slot][col] == 'o':  
            available_tables.append(restaurant_schedule[0][col]) 
    
    return available_tables  


def find_table(restaurant_schedule, time_slot, num_guests):
    available_tables = get_open_tables(restaurant_schedule, time_slot)

 
    for table in available_tables:
        try:
            capacity = int(table.split('(')[1].split(')')[0]) 
        except (IndexError, ValueError):
            print(f"Warning: Couldn't extract capacity from {table}") 
            continue 

        if capacity >= num_guests:
            return table  
    
    return None  


restaurant_schedule = [
    [0,         'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    [1,         'x',     'o',     'o',     'o',     'o',     'x'],
    [2,         'o',     'x',     'o',     'o',     'x',     'o'],
    [3,         'x',     'x',     'o',     'x',     'o',     'o'],
    [4,         'o',     'o',     'o',     'x',     'o',     'x'],
    [5,         'o',     'x',     'o',     'x',     'o',     'o'],
    [6,         'o',     'o',     'o',     'o',     'x',     'o']
]


requested_time_slot = 2
group_size = 10


best_table = find_table(restaurant_schedule, requested_time_slot, group_size)


if best_table:
    print(f"A suitable table for {group_size} people at timeslot {requested_time_slot} is: {best_table}")
else:
    print(f"No suitable table found for {group_size} people at timeslot {requested_time_slot}")
