with open('input.txt ') as f:
    content = f.read()
    
num = 0
for char in content:
    if char.isalpha():
        num += 1

print(f'Part 1: {num}')