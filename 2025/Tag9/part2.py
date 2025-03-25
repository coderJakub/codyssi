with open('input.txt') as f:
    balance, transactions = f.read().split('\n\n')
    
balance = {line.split(' HAS ')[0]: int(line.split(' HAS ')[1]) for line in balance.split('\n')}

for transaction in transactions.split('\n'):
    sender = transaction.split(' TO ')[0][5:]
    empf = transaction.split(' TO ')[1].split(' AMT ')[0]
    bal = min(int(transaction.split(' TO ')[1].split(' AMT ')[1]), balance[sender])
    
    balance[sender] -= bal
    balance[empf] += bal
    
richest = sorted(balance.items(), key=lambda x: x[1], reverse=True)[:3]
print(f'Part 2: {sum([x[1] for x in richest])}')
