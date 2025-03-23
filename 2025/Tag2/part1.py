with open("input.txt") as f:
    input = f.read().split("\n")

nums = input[4:]
median = int(sorted(nums)[len(nums)//2])
print(f'Part 1: {(median**3)*61+256}')