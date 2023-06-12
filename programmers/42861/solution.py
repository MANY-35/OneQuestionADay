n = 5
costs =  [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]


def find(table, x):
    if table[x] == x:
        return x
    table[x] = find(table, table[x])
    return table[x]
def union(table, a, b):
    A = find(table, a)
    B = find(table, b)
    
    if A < B:
        table[B] = A
    else:
        table[A] = B    
    
answer = 0
table = [i for i in range(n)]
for s,e,c in sorted(costs, key=lambda x:(x[-1],x[0])):
    if find(table, s) != find(table, e):
        union(table, s, e)
        answer += c
print(answer)