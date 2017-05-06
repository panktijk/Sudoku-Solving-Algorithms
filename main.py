import time
from getpuzzles import get_puzzles_list_CP, get_puzzles_list_BF
from sudokuCP import solve_CP, solve_DFS_CP, display
from sudokuBF import solve_BF
import matplotlib.pyplot as plt
import numpy as np

def solve_single_puzzle(method, grid):
    start_time = time.clock()  
    solution = method(grid)
    elapsed = time.clock() - start_time
    print('Time taken: ' + str(elapsed))
    return solution
    
def solve_puzzles_list(method, puzzles):
    num_of_puzzles = len(puzzles)
    start_time = time.clock()  
    count = 1
    for puzzle in puzzles:
        method(puzzle)
        print(str(count) + ' out of ' + str(num_of_puzzles) + ' puzzles solved')
        count+=1
    elapsed = time.clock() - start_time
    print('Total time taken: ' + str(elapsed))
    return elapsed
    
def plot_times(x, y, title):
    plt.figure()
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.xlabel('Method used')
    plt.ylabel('Time taken')
    plt.title(title) 
    plt.show()

easy_test_grid = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'

print("Easy Test puzzle solved by Brute Force:")
p = list(easy_test_grid)
easy_test_grid_BF = [p[i:i + 9] for i in xrange(0, len(p), 9)] 
solve_single_puzzle(solve_BF, easy_test_grid_BF)

print("\nEasy Test puzzle solved by Constraint Propagation:")
display(solve_single_puzzle(solve_CP, easy_test_grid))

print("\nEasy Test puzzle solved by DFS and Propagation:")
display(solve_single_puzzle(solve_DFS_CP, easy_test_grid))

hard_test_grid = '400000805030000000000700000020000060000080400000010000000603070500200000104000000'

print("\nHard Test puzzle solved by Brute Force:")
p = list(hard_test_grid)
hard_test_grid_BF = [p[i:i + 9] for i in xrange(0, len(p), 9)] 
#solve_single_puzzle(solve_BF, hard_test_grid_BF)

print("\nHard Test puzzle solved by Constraint Propagation:")
display(solve_single_puzzle(solve_CP, hard_test_grid))

print("\nHard Test puzzle solved by DFS and Propagation:")
display(solve_single_puzzle(solve_DFS_CP, hard_test_grid))

easy_puzzles = get_puzzles_list_CP('easy_puzzles.txt')
easy_puzzles_BF = get_puzzles_list_BF('easy_puzzles.txt')
easy_puzzles_time = []

print('\nSolved by Brute Force:')
easy_puzzles_time.append(solve_puzzles_list(solve_BF, easy_puzzles_BF))

print("\nSolved by Constraint Propagation:")
easy_puzzles_time.append(solve_puzzles_list(solve_CP, easy_puzzles))

print("\nSolved by DFS and Propagation:")
easy_puzzles_time.append(solve_puzzles_list(solve_DFS_CP, easy_puzzles))

x = ['BF', 'CP', 'DFS with CP']
plot_times(x, easy_puzzles_time, '50 Easy Puzzles')

hard_puzzles = get_puzzles_list_CP('hard_puzzles.txt')
hard_puzzles_BF = get_puzzles_list_BF('hard_puzzles.txt')
hard_puzzles_time = []

print('\nSolved by Brute Force:')
hard_puzzles_time.append(solve_puzzles_list(solve_BF, hard_puzzles_BF))

print("\nSolved by Constraint Propagation:")
hard_puzzles_time.append(solve_puzzles_list(solve_CP, hard_puzzles))

print("\nSolved by DFS and Propagation:")
hard_puzzles_time.append(solve_puzzles_list(solve_DFS_CP, hard_puzzles))

x = ['BF', 'CP', 'DFS with CP']
plot_times(x, hard_puzzles_time, '10 Hard Puzzles')
