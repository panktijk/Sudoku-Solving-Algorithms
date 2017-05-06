def get_puzzles_list_CP(file_name):
    with open(file_name) as f:
        puzzles = f.readlines()
    return [puzzle.strip() for puzzle in puzzles]
    
def get_puzzles_list_BF(file_name):
    puzzles = []
    with open(file_name) as f:
        for line in f:
            p = list(line.strip())
            puzzle = [p[i:i + 9] for i in xrange(0, len(p), 9)] 
            puzzles.append(puzzle)
        return puzzles