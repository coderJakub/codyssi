with open('input.txt') as file:
    content = file.read().split('\n')

num = 0

for line in content:
    for char in line:
        num += ord(char) - ord('A')+1

print(f'Part 1: {num}')