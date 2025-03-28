with open('input.txt') as f:
    gridS, instrs, flow_control = f.read().split('\n\n')
    
grid = [[int(c) for c in line.split(" ")] for line in gridS.split("\n")]

def shift(inst):
    [rc, idx,_, am] = inst
    idx, am = int(idx), int(am)
    temp = grid
    if rc == "COL":
        temp = [list(k) for k in list(zip(*grid))]
    for i in range(am):
        temp[idx-1].insert(0, temp[idx-1].pop())
    if rc == "COL":
        return [list(k) for k in list(zip(*temp))]
    return temp

def maths(inst):
    if inst[2] == "ALL":
        [op, am, rc] = inst
    else:
        [op, am, rc, idx] = inst
    for i,line in enumerate(grid):
        for j,char in enumerate(line):
            if rc=="ALL" or rc=="COL" and j+1==int(idx) or rc=="ROW" and i+1==int(idx):
                match op:
                    case "SUB":
                        grid[i][j] = char-int(am)
                    case "ADD":
                        grid[i][j] = char+int(am)
                    case "MULTIPLY":
                        grid[i][j] = char*int(am)
                while not 0<=grid[i][j]<=1073741823:
                    if grid[i][j] <= 0:
                        grid[i][j]+=1073741824
                    elif grid[i][j] >= 1073741823:
                        grid[i][j]-=1073741824
    return grid

take = None
instrs = instrs.split("\n")
for cc in flow_control.split("\n"):
    match cc:
        case "TAKE":
            take = instrs[0]
            instrs = instrs[1:]
        case "CYCLE":
            assert take
            instrs.append(take)
        case "ACT":
            assert take
            if take.split(" ")[0] == "SHIFT":
                grid = shift(take.split(" ")[1:])
            else:
                grid = maths(take.split(" "))

print(f'Part 2: {max(max([sum(line) for line in grid]), max([sum(line) for line in list(zip(*grid))]))}')