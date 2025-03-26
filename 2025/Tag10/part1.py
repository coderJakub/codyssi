with open('input.txt') as f:
    content = [[int(c) for c in line.split(" ")]for line in f.read().split('\n')]
    
minRow = min([sum(row) for row in content])
minCol = min([sum(col) for col in list(zip(*content))])
print(f'Part 1: {min(minRow, minCol)}')