rows = 100
columns = 97
queries = [[1,1,100,97]]

from collections import deque

arr = [[(j*columns) + i for i in range(1, columns+1)] for j in range(rows)]
answer = []
for query in queries:
    q = [i-1 for i in query]
    print(arr)
    dque = deque([])
    
    for x in range(q[1], q[3]):
        dque.append(arr[q[0]][x])
    for y in range(q[0], q[2]):
        dque.append(arr[y][q[3]])
    for x in range(q[3], q[1], -1):
        dque.append(arr[q[2]][x])
    for y in range(q[2], q[0], -1):
        dque.append(arr[y][q[1]])
    
    print(dque)
    
    answer.append(min(dque))
    dque.appendleft(dque.pop())
    print(dque)
    
    
    for x in range(q[1], q[3]):
        arr[q[0]][x] = dque.popleft()
    for y in range(q[0], q[2]):
        arr[y][q[3]] = dque.popleft()
    for x in range(q[3], q[1], -1):
        arr[q[2]][x] = dque.popleft()
    for y in range(q[2], q[0], -1):
        arr[y][q[1]] = dque.popleft()
    
print(answer)