from collections import defaultdict

with open('input.txt') as f:
    grid = [[int(c) for c in line.split(" ")]for line in f.read().split('\n')]
    
start = grid[0][0]

R = len(grid)
C = len(grid[0])

def dijkstra(start):
    gridDanger = defaultdict(lambda: float('inf'))
    visited = set()
    
    gridDanger[(0,0)] = start
    
    while True:
        minDanger = float('inf')
        minCoords = None
        for coords, danger in gridDanger.items():
            if coords not in visited and danger < minDanger:
                minDanger = danger
                minCoords = coords
        
        if minCoords == (R-1, C-1):
            return minDanger
        
        visited.add(minCoords)
        
        for dR, dC in [(0,1),(1,0)]:
            newCoords = (minCoords[0]+dR, minCoords[1]+dC)
            if 0 <= newCoords[0] < R and 0 <= newCoords[1] < C:
                gridDanger[newCoords] = min(gridDanger[newCoords], minDanger+grid[newCoords[0]][newCoords[1]])
            
print(f'Part 3: {dijkstra(start)}')