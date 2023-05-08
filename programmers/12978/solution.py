N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

arr = [[500001 for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i][i] = 0
    

for d0, d1, d2 in road:
    arr[d0-1][d1-1] = min(d2, arr[d0-1][d1-1])
    arr[d1-1][d0-1] = min(d2, arr[d1-1][d0-1])

for k in range(N):
    for l in range(N):
        for i in range(N):
            arr[l][i] = arr[i][l] = min(arr[l][i], arr[l][k] + arr[k][i])

for i in arr:
    print(i)

answer = 0
for i in arr[0]:
    if i <= K:
        answer += 1
print(answer)