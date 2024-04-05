
import random

from copy import deepcopy
#------------------------------------------------------------------------------

def print_nested_list_horizontally(nested_list):
    transposed_list = zip(*nested_list)
    for row in transposed_list:
        print(" ".join(row))

#------------------------------------------------------------------------------
def remove_subset_tuples(data):
    cleaned_data = set()
    for entry in data:
        is_subset = False
        for other_entry in data:
            if entry != other_entry and isinstance(entry[2], tuple) and isinstance(other_entry[2], tuple):
                if set(entry[2]).issubset(other_entry[2]):
                    is_subset = True
                    break
        if not is_subset:
            cleaned_data.add(entry)
    return cleaned_data


#------------------------------------------------------------------------------
def consec(string):
    count = 1
    for i in range(1, len(string)):
        if string[i] != string[0]:
            return string[0], count
        count += 1
    return string[0], count

#------------------------------------------------------------------------------
def check_winline(grid, winlines):
    unique_check = set()
    lines = []
    grid_x = []
    for winline_index, winline in enumerate(winlines):
        symbols = [grid[row][col] for row, col in winline]
        new_grid = deepcopy(grid)
        for row, col in winline:
            new_grid[row][col] = '■'

        line_str = ''.join(symbols)
        symbol, count = consec(line_str)

        if count > 1 and tuple(winline) not in unique_check:
            unique_check.add(tuple(winline))
            lines.append((symbol, count, tuple(winline)))
            grid_x.append(new_grid)
    if debug:
        for element in grid_x:
            print_nested_list_horizontally(element)
            print(':::::::::')

    return lines



  
#------------------------------------------------------------------------------
def total_win(result):
  total_sum = 0
  for win in result:
    total_sum += paytable[win[0]][win[1]]
  return total_sum


#------------------------------------------------------------------------------
def spin_result(reels):
  grid = []
  for reel in reels:
    reel_length = len(reel)
    start_index = random.randint(0, reel_length - 1)
    column = [reel[(start_index + i) % reel_length] for i in range(3)]
    grid.append(column)
  return grid
#------------------------------------------------------------------------------
def game_sim(num_trials, reel, winlines):
    count_matches = 0
    payout = 0
    print("Starting simulation...")
    for trial in range(num_trials):
        grid = spin_result(reel)
        result = check_winline(grid, winlines)
     #  result = remove_subset_tuples(check_winline(grid, winlines))
        if debug:
            print("Debug is enabled.")
            print_nested_list_horizontally(grid)
            print('Symbol, max path length and path recognized:')
            print(result)
            print(total_win(result))
                
            print('---------------------')
        

        if result and total_win(result) > 0:
            count_matches += 1
            payout += total_win(result)
        if not debug:
                if (trial + 1) % (num_trials //100) == 0:
                    progress_percentage = ((trial + 1) / num_trials) * 100
                    print(f"Progress: {progress_percentage:.0f}%")
        

    print("Simulation complete.")
    print("Total wins:", count_matches)
    print("Percentage winning spins:", (count_matches / num_trials) * 100, "%")
    print("Total win:", payout)
    print("Total bet (#spins)", num_spins)
    print("RTP:", payout/num_spins)



# Setup 
#------------------------------------------------------------------------------


#reel_0 = ['3', '1', '3', '3']
#reel_1 = ['5', '1', '5', '5']
#reel_2 = ['1', '1', '1', '3']
#reel_3 = ['0', '0', '2', '3']
#reel_4 = ['0', '0', '2', '3']


reel_0 = ['1', '5', '3', '4', '5', '4', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '1', '0', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '2', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '4', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3']
reel_1 = ['1', '3', '5', '0', '2', '3', '4', '5', '4', '1', '0', '3', '5', '0', '5', '4', '0', '2', '5', '1', '0', '5', '1', '5', '3', '4', '5', '3', '1', '3', '5', '4', '0', '3', '5', '2', '3', '4', '3', '2', '3', '4', '5', '3', '1', '0', '4', '5', '1', '5', '4', '3', '2', '4', '5', '4', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '1', '2', '3', '4', '5', '2', '1', '0', '4', '5', '1', '5', '4', '3', '2', '5', '1', '0', '5', '1', '2', '3', '4', '5', '3', '1', '3', '5', '3', '5', '3', '5', '2', '3']
reel_2 = ['0', '5', '2', '4', '5', '4', '0', '2', '5', '4', '2', '3', '5', '0', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '2', '4', '2', '5', '3', '1', '3', '4', '2', '4', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '4', '0', '4', '3', '2', '4', '1', '0', '5', '1', '4', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '4', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '2']
reel_3 = ['1', '5', '3', '4', '5', '4', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '1', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '2', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '4', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3']
reel_4 = ['1', '5', '3', '4', '5', '4', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '1', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '2', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3', '2', '4', '1', '0', '5', '1', '4', '3', '4', '5', '3', '1', '3', '5', '4', '2', '3', '5', '2', '3', '4', '0', '2', '3', '4', '5', '2', '1', '0', '4', '5', '0', '5', '4', '3']




reels = [reel_0, reel_1, reel_2, reel_3, reel_4]

winlines = [

    [(0,0), (1,0), (2,0), (3,0), (4,0)],
    [(0,1), (1,1), (2,1), (3,1), (4,1)],
    [(0,2), (1,2), (2,2), (3,2), (4,2)],


    [(0,0), (1,0), (2,1), (3,0), (4,0)],
    [(0,1), (1,1), (2,0), (3,1), (4,1)],
    [(0,2), (1,2), (2,1), (3,2), (4,2)],
    [(0,1), (1,1), (2,2), (3,1), (4,1)],

    [(0,0), (1,1), (2,0), (3,1), (4,0)],
    [(0,1), (1,0), (2,1), (3,0), (4,1)],
    [(0,2), (1,1), (2,2), (3,1), (4,2)],
    [(0,1), (1,2), (2,1), (3,2), (4,1)],


    [(0,0), (1,1), (2,1), (3,1), (4,0)],
    [(0,1), (1,0), (2,0), (3,0), (4,1)],
    [(0,2), (1,1), (2,1), (3,1), (4,2)],
    [(0,1), (1,2), (2,2), (3,2), (4,1)],

    [(0,0), (1,1), (2,2), (3,1), (4,0)],
    [(0,2), (1,1), (2,0), (3,1), (4,2)],

    [(0,0), (1,2), (2,1), (3,0), (4,2)],
    [(0,2), (1,0), (2,1), (3,2), (4,0)],

    [(0,1), (1,0), (2,2), (3,0), (4,1)]

]
     

paytable = {
    '0': {0:0 , 1:0 , 2:0.5 , 3:2.5 , 4:6  , 5:25},
    '1': {0:0 , 1:0 , 2:0.3 , 3:1.7 , 4:4  , 5:20},
    '2': {0:0 , 1:0 , 2:0.3 , 3:1.2 , 4:3  , 5:15},
    '3': {0:0 , 1:0 , 2:0   , 3:0.7 , 4:2  , 5:7 },
    '4': {0:0 , 1:0 , 2:0   , 3:0.6 , 4:1.5, 5:6 },
    '5': {0:0 , 1:0 , 2:0   , 3:0.5 , 4:1.2, 5:5 }
}

# Sim
#------------------------------------------------------------------------------

num_spins = 100000
debug = 0

# Output
#------------------------------------------------------------------------------
game_sim(num_spins, reels, winlines)


