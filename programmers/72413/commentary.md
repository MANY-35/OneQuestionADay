# Lv2 합승 택시 요금

### 1차 시도 (성공)
```py
def solution(n, s, a, b, fares):
    n+=1
    inf = 1000001
    arr = [[inf]*n for _ in range(n)]
    for i in range(n):
        arr[i][i] = 0
    for start, dest, cost in fares:
        arr[start][dest] = cost
        arr[dest][start] = cost
    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
    answer = arr[s][b] + arr[s][a]
    for i in range(1, n):
        answer = min(answer, arr[s][i]+arr[i][a]+arr[i][b])
    return answer
```
노드의 갯수가 최대 200인 것으로 플로이드 워셜알고리즘이 O(n^3)이라고 생각했을때 충분히 가능할 것 같다고 판단하여 알고리즘을 사용하여 풀었다.  
>알고리즘을 적용시키기 전에는 dfs와 bfs를 결합하여 풀어볼 생각을 했는데 생각하는 것과 다르게 코드로 구현하는데 어려움이 생겨 풀지 못했다.  
이 코드로 시간이 평균 2,500ms 정도 나오는 것이 마음에 걸려 다른 사람들의 코드를 구경했는데 그중 다익스트라를 a, b, s에서 구해서 구하는 방법이 있다는 것을 보고 아직 멀었다고 생각했다.
