with open('input.txt ') as f:
    content = f.read()
    
num = 0
prev = 0
for char in content:
    if char.isalpha():
        if char.isupper():
            num += ord(char) - ord('A') + 27
        else:
            num += ord(char) - ord('a') + 1
    
print(f'Part 2: {num}')