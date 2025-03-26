with open('input.txt') as f:
    data = f.read().split('\n')
    
num = 0
for line in data:
    for boxrange in line.split(' '):
       num += int(boxrange.split('-')[1]) - int(boxrange.split('-')[0])+1
       
print(num)