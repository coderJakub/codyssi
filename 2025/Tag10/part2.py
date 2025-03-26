with open('input.txt') as f:
    grid = [[int(c) for c in line.split(" ")]for line in f.read().split('\n')]
    
start = grid[0][0]
queue = [(grid[0][0],(0,0))]
visited = set()
while queue:
    queue.sort(key=lambda x: x[0])
    dangerLevel, coords = queue.pop(0)
    visited.add(coords)
    
    if coords == (14,14):
        print(f'Part 2: {dangerLevel}')
        exit()
    
    if coords[0]+1 < 15 and (coords[0]+1, coords[1]) not in visited:
        queue.append((dangerLevel+grid[coords[0]+1][coords[1]], (coords[0]+1, coords[1])))
    if coords[1]+1 < 15 and (coords[0], coords[1]+1) not in visited:
        queue.append((dangerLevel+grid[coords[0]][coords[1]+1], (coords[0], coords[1]+1)))