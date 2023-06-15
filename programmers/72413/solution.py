from collections import deque
n=6
s=4
a=6
b=2
fares =	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


n+=1
inf = 1000001

path = [[] for _ in range(n)]
arr = [[inf]*n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0
for start, dest, cost in fares:
    arr[start][dest] = cost
    arr[dest][start] = cost
    path[start].append(dest)
    path[dest].append(start)
    
for k in range(1,n):
    for i in range(1,n):
        for j in range(1,n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in arr:
    print(i)

m = arr[s][b] + arr[s][a]

for i in range(1, n):
    m = min(m, arr[s][i]+arr[i][a]+arr[i][b])
print(m)
    
    