
def snake(grid):
    directions = {
        (0, 1): 'right',
        (1, 0): 'down',
        (0, -1): 'left',
        (-1, 0): 'up'
    }
    start = None
    # find start position
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '$':
                start = (i, j)
                break
        if start:
            break
    

    visitedSet = set()
    stack = [(start, "")]
    
    while stack:
        (i, j), path = stack.pop()
        if grid[i][j] == 'F':
            return path
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                continue
            if grid[ni][nj] in {'+', '-', '|'}:
                continue
            if (ni, nj) in visitedSet:
                continue
            visitedSet.add((ni, nj))
            stack.append(((ni, nj), path + directions[(di, dj)] + " "))
    
    return "No path found"


maze = [['+', '-', '+', '-', '+', '-', '+'],

['|', ' ', ' ', ' ', ' ', ' ', '|'],

['+', ' ', '+', '-', '+', ' ', '+'],

['|', '  ', ' ', 'F', '|', ' ', '|'],

['+', '-', '+', '-', '+', ' ', '+'],

['|', '$', ' ', ' ', ' ', ' ', '|'],

['+', '-', '+', '-', '+', '-', '+']]

print(snake(maze))