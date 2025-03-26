with open('input.txt') as f:
    content = f.read().split('\n')

def getSmallest(content, pos):
    minH = float('inf')
    xmin,ymin = pos
    for x,y in content:
        abst = abs(x-pos[0]) + abs(y-pos[1])
        if abst <= minH or (abst == minH and x<xmin) or (abst == minH and x==xmin and y<ymin):
            minH = abst
            xmin,ymin = x,y
    return xmin,ymin

islands = [[int(line[1:-1].split(',')[0]),int(line[1:-1].split(',')[1])] for line in content]
sortedList = []
x,y = 0,0
while islands:
    x,y = getSmallest(islands, [x,y])
    sortedList.append([x,y])
    islands.remove([x,y])

num = 0
x,y = 0,0
for xn,yn in sortedList:
    num += abs(x-xn) + abs(y-yn)
    x,y = xn,yn

print(f'Part 3: {num}')