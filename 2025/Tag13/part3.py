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
    
def dfs(cycle, length=0):
    maxCycle = 0
    if cycle[-1] not in paths.keys():
        return 0
    for [neighbor,l] in paths[cycle[-1]]:
        if neighbor == cycle[0]:
            maxCycle = max(maxCycle, length+l)
        elif neighbor not in cycle:
            maxCycle = max(dfs(cycle+[neighbor], length+l), maxCycle)
    return maxCycle

maxCycle = 0
for k in paths.keys():
    maxCycle = max(maxCycle, dfs([k]))
    
print(f'Part 3: {maxCycle}')