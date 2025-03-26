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
x1,y1 = getSmallest(islands, [0,0])
islands.remove([x1,y1])
x2,y2 = getSmallest(islands, [x1,y1])
print(f'Part 2: {abs(x1-x2)+abs(y1-y2)}')