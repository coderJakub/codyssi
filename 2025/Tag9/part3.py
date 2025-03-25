with open('input.txt') as f:
    balance, transactions = f.read().split('\n\n')
    
balance = {line.split(' HAS ')[0]: int(line.split(' HAS ')[1]) for line in balance.split('\n')}

debts = {p:[] for p in balance.keys()}  

transactions = [(transaction.split(' TO ')[0][5:], transaction.split(' TO ')[1].split(' AMT ')[0], int(transaction.split(' TO ')[1].split(' AMT ')[1])) for transaction in transactions.split('\n')]

def transact(transaction):
    sender, empf, amount = transaction
    if amount > balance[sender]:
        debt = amount - balance[sender]
        amount = balance[sender]
        debts[sender].append((empf, debt))
    
    balance[sender] -= amount
    balance[empf] += amount
    
    
    while debts[empf] and balance[empf] > 0:
        assert len(debts[empf]) > 0
        debt = debts[empf][0][1]
        transfer = min(debt, balance[empf])
        
        if transfer == debt:
            temp = debts[empf].pop(0)
            trans = (empf, temp[0], transfer)
        else:
            debts[empf][0] = (debts[empf][0][0], debt - transfer)
            trans = (empf, debts[empf][0][0], transfer)
        transact(trans)

for transaction in transactions:
    transact(transaction)
            
richest = sorted(balance.items(), key=lambda x: x[1], reverse=True)[:3]
print(f'Part 3: {sum([x[1] for x in richest])}')