with open("input.txt") as f:
    input = f.read().split("\n")
    
num = sum([int(numb) if int(numb)%2==0 else 0 for numb in input[4:]])
print((num**3)*61+256)