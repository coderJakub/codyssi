with open('input.txt') as file:
    content = file.read().split('\n')
    
def getNumber(char:str):
    if char.isnumeric():
        return int(char)
    if ord('A') <= ord(char) <= ord('Z'):
        return ord(char)-ord('A')+10
    return ord(char)-ord('a')+36

maxVal = 0
for line in content:
    val, base = line.split(" ")
    num = 0
    for i,char in enumerate(val[::-1]):
        num+=getNumber(char)*int(base)**i
    maxVal = max(maxVal, num)

print(f'Part 1: {maxVal}')