import time

def clear(number, r, c, grid):
    if number in grid[r]:
        return False
    if number in [row[c] for row in grid]:
        return False
    row_start = r - r%3
    row_end = row_start + 3
    col_start = c - c%3
    col_end = col_start + 3
    square = [row[col_start:col_end] for row in grid[row_start:row_end]]
    for row in square:
        if number in row:
            return False
    return True

def recurse(r, c, grid):
    if r>8:
        return grid

    if grid[r][c] == '0':
        for number in '123456789':
            if clear(number, r, c, grid):
                grid[r] = grid[r][0:c] + [number] + grid[r][c+1:]           
                c += 1
                if c > 8:
                    r += 1
                    c = 0
                solution= recurse(r, c, grid)
                if solution:
                    return solution
                c -= 1
                if c < 0:
                    r -= 1
                    c = 8
                grid[r] = grid[r][0:c] + ['0'] + grid[r][c+1:]      
    else:
        c += 1
        if c > 8:
            r += 1
            c = 0
        return recurse(r, c, grid)
        
def solve_BF(grid):
    return recurse(0, 0, grid)
