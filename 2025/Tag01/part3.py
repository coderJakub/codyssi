with open("input.txt", "r") as file:
    input = file.read().split("\n")

instructions = []
for line in range(0,len(input[:-1]),2):
    instructions.append(input[line]+input[line+1])

num = int(instructions[0])
for line, sign in zip(instructions[1:], reversed(input[-1])):
    match sign:
        case "-": num -= int(line)
        case "+": num += int(line)
        
print(f'Part 3: {num}')