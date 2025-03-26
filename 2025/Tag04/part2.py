with open('input.txt') as file:
    content = file.read().split('\n')

num = 0

for line in content:
    l = len(line)//10
    lm = str(len(line)-2*l)
    num += sum(int(k) for k in str(lm)) + sum(ord(char)-ord('A')+1 for char in line[:l]+line[-l:])
 
print(f'Part 2: {num}')