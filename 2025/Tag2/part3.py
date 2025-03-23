with open("input.txt") as f:
    input = f.read().split("\n")
    
highest = 0
for line in input:
    lineV = (((int(line)**3)*61)+256)
    if lineV < 15000000000000:
        highest = max(int(line), highest)

print(f'Part 3: {highest}')