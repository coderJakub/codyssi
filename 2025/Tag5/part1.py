with open('input.txt') as f:
    content = f.read().split('\n')

minH = float('inf')
maxH = 0
for line in content:
    x,y = line[1:-1].split(',')
    abst = abs(int(x)) + abs(int(y))
    minH = min(minH, abst)
    maxH = max(maxH, abst)
    
print(f'Part 1 {maxH-minH}')