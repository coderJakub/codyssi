from functools import cmp_to_key
with open("input.txt") as f:
    content = f.read().split("\n")

itemsInfo = {}
items = []
for line in content:
    parts = line.split(" ")
    itemid = int(parts[0])
    code = parts[1]
    quality = int(parts[5][:-1])
    costs = int(parts[8][:-1])
    materials = int(parts[12])
    itemsInfo[code] = {"id": itemid, "quality": quality, "costs": costs, "materials": materials}
    items.append(code)

def letter_cmp(a, b):
    if itemsInfo[a]["quality"] == itemsInfo[b]["quality"]:
        return -1 if itemsInfo[a]["costs"]>itemsInfo[b]["costs"] else 1
    return -1 if itemsInfo[a]["quality"]>itemsInfo[b]["quality"] else 1
letter_cmp_key = cmp_to_key(letter_cmp)
items.sort(key = letter_cmp_key)

sol = 0
for i in range(5):
    sol += itemsInfo[items[i]]["materials"]
print(sol)