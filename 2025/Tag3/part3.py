with open('input.txt') as f:
    data = f.read().split('\n')
    
pilabels = []
for line in data:
    boxlabels = set()
    for boxrange in line.split(' '):
        for i in range(int(boxrange.split('-')[0]), int(boxrange.split('-')[1])+1):
            boxlabels.add(i)
    pilabels.append(boxlabels)

maxL = 0
for i,pilabel in enumerate(pilabels[:-1]):
    pilabel2 = pilabels[i+1]
    print(pilabel.union(pilabel2))
    maxL = max(maxL, len(pilabel.union(pilabel2)))
       
print(maxL)