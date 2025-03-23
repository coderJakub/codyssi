with open("input.txt", "r") as file:
    input = file.read().split("\n")

num = int(input[0])
for line, sign in zip(input[1:-1], input[-1]):
    match sign:
        case "-": num -= int(line)
        case "+": num += int(line)
        
print(f'Part 1: {num}')