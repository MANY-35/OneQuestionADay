# LV3 가장 먼 노드

### 1차시도 (실패)
```py
def solution(n, edge):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for a, b in edge:
        a-=1
        b-=1
        arr[a][b] = 1
        arr[b][a] = 1
    que = [0]
    vist = [0]
    while que:
        t = []
        while que:
            n = que.pop()
            for i in range(len(arr[n])):
                if i not in vist and arr[n][i] == 1:
                    t.append(i)
                    vist.append(i)
        if t != []:
            c = len(t)
        que = t
    return c
```
bfs와 유사한 방식으로 풀어 봤는데 3개의 케이스에서 시간초과가 발생했다. 

*****

### 2차시도 (성공)
```py
def solution(n, edge):
    vist = [True for _ in range(n)]
    arr = [[] for _ in range(n)]
    for a, b in edge:
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)
    que = [[0]]
    vist[0] = False
    while que[-1]:
        t = []
        for i in que[-1]:
            for j in range(len(arr[i])):
                if vist[arr[i][j]]:
                    t.append(arr[i][j])
                    vist[arr[i][j]] = False
        que.append(t)
    return len(que[-2])
```
이전 코드에서 vist배열에 저장하면서 안에 존재하는지 여부를 판단하는 것이 아니라 모든 노드에 vist를 부여하여 방문을 했는지 판단하는 방식으로 바꿔서 시간을 많이 줄였다.  
또한 n*n배열로 간선을 확인하는 것이 아니라 n번째 노드에서 갈 수 있는 노드들을 저장하는 방식으로 시간을 줄였다.