from collections import defaultdict

with open('input.txt') as f:
    content = f.read().split('\n')
    
paths = defaultdict(list)
shortest = {}
for line in content:
    a = line.split(' -> ')[0]
    b = line.split(' -> ')[1].split(' | ')[0]
    length = int(line.split(' | ')[1])
    paths[a].append([b, length])
    shortest[a] = float('inf')
    shortest[b] = float('inf')
    
visited = set()
shortest['STT'] = 0
while len(visited) < len(paths.keys()):
    minLength = float('inf')
    nextRegion = None
    for region, length in shortest.items():
        if minLength > length and region not in visited:
            minLength = length
            nextRegion = region
    
    visited.add(nextRegion)
    
    for [val, l] in paths[nextRegion]:
        shortest[val] = min(minLength+l, shortest[val])

paths = sorted(shortest.values())[::-1]

sol = 1
for i in range(3):
    sol*=paths[i]

print(f'Part 2: {sol}')