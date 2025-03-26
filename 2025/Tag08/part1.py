with open('input.txt') as f:
    lines = f.read()
    
print(sum(1 if c.isalpha() else 0 for c in lines))