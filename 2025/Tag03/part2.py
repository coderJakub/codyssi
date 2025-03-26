with open('input.txt') as f:
    data = f.read().split('\n')
    
num = 0
for line in data:
    boxlabels = set()
    for boxrange in line.split(' '):
        for i in range(int(boxrange.split('-')[0]), int(boxrange.split('-')[1])+1):
            boxlabels.add(i)
    num += len(boxlabels)
       
print(num)