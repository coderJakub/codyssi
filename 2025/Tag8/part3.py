import re
with open('input.txt') as f:
    lines = f.read().split('\n')

num = 0
for line in lines:
    newLine = ""
    for i,c in enumerate(line):
        if newLine and (c.isdigit() and newLine[-1].isalpha() or c.isalpha() and newLine[-1].isdigit()):
            newLine = newLine[:-1]
        else:
            newLine += c
    num += len(newLine)
    
print(num)