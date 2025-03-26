with open('input.txt') as file:
    content = file.read().split('\n')

num = 0

for line in content:
    count = 1
    for idx,char in enumerate(line[1:]):
        if char != line[idx]:
            num += sum(int(k) for k in str(count)) + ord(line[idx])-ord('A')+1
            count = 1
        else:
            count += 1
    num += sum(int(k) for k in str(count)) + ord(line[-1])-ord('A')+1

print(f'Part 3: {num}')