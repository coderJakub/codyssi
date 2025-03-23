with open('input.txt ') as f:
    content = f.read()
    
num = 0
prev = 0
for char in content:
    if char.isalpha():
        if char.isupper():
            numA = ord(char) - ord('A') + 27
        else:
            numA = ord(char) - ord('a') + 1
    else:
        temp = prev*2-5
        while temp < 1:
            temp += 52
        while temp > 52:
            temp -= 52
        numA = temp
    prev = numA
    num += numA        
print(f'Part 3: {num}')