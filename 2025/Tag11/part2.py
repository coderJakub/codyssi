with open('input.txt') as file:
    content = file.read().split('\n')
    
def getNumber(char:str):
    if char.isnumeric():
        return int(char)
    if ord('A') <= ord(char) <= ord('Z'):
        return ord(char)-ord('A')+10
    return ord(char)-ord('a')+36

def getChar(num):
    if 0<=num<=9:
        return str(num)
    if 10<=num<=35:
        return chr(num-10+ord('A'))
    if 36<=num<=61:
        return chr(num-36+ord('a'))
    return{62:'!', 63:'@', 64:'#', 65:'$', 66:'%', 67:'^'}[num]

sumVal = 0
for line in content:
    val, base = line.split(" ")
    num = 0
    for i,char in enumerate(val[::-1]):
        num+=getNumber(char)*int(base)**i
    sumVal += num
    
base68 = ""
while sumVal>0:
    base68 = getChar(sumVal%68)+base68
    sumVal = sumVal//68

print(f'Part 2: {base68}')