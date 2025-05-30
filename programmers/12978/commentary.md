# LV2 두 큐 합 같게 하기

### 1차 시도 (실패)
```py
def solution(N, road, K):
    m = [[K*K, []] for i in range(N+1)]
    for data in road:
        s, e = (data[0], data[1]) if data[1]>data[0] else (data[1],data[0])
        m[s][-1].append([e, data[2]])

    m[1][0] = 0
    for i in range(1, len(m)):
        for j in m[i][-1]:
            m[j[0]][0] = min(m[i][0] + j[1], m[j[0]][0])

    answer = 0
    for i in range(1,len(m)):
        if m[i][0] <= K:
            answer += 1
    return answer
```
> 반의 반 정도의 데이터 케이스만 정답이 되었다. 절반 이상이 틀린 것이면 코드 자체에 문제가 있다고 볼 수 있다. 모든 도로를 단방향으로 생각하고 풀어서 생긴 문제 같다.

*****

### 2차 시도 (실패)
```py
def solution(N, road, K):
    m = [[K*K, []] for i in range(N+1)]
    for data in road:
        d1, d2 = data[0], data[1]
        m[d1][-1].append([d2, data[2]])
        m[d2][-1].append([d1, data[2]])

    m[1][0] = 0
    for i in range(1, len(m)):
        for j in m[i][-1]:
            m[j[0]][0] = min(m[i][0] + j[1], m[j[0]][0])

    answer = 0
    for i in range(1,len(m)):
        if m[i][0] <= K:
            answer += 1
    return answer
```
> 도로를 양방향으로 설정하고 풀이를 해보았지만 절반 정도의 데이터 케이스에서 실패했다.

*****

### 3차 시도 (실패)
```py
def solution(N, road, K):
    arr = [[10001 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i][i] = 0

    for data in road:
        d0 = data[0]-1
        d1 = data[1]-1
        arr[d0][d1] = arr[d1][d0] = min(data[2], arr[d0][d1])

    for k in range(N):
        for l in range(N):
            for i in range(N):
                arr[l][i] = arr[i][l] = min(arr[l][i], arr[l][k] + arr[k][i])

    answer = 0
    for i in arr[0]:
        if i <= K:
            answer += 1
    return answer
```
> 3개의 데이터 케이스가 실패했다.

*****

### 4차 시도 (성공)
```py
def solution(N, road, K):
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
                
    answer = 0
    for i in arr[0]:
        if i <= K:
            answer += 1
    return answer
```
3차 시도에서 길의 초기값을 길의 최댓값인 10,000보다 1 큰 10,001로 설정했는데, 문제는 배달 가능한 시간이 500,000이기 때문에 갈 수 없는 길이라는 뜻인 10,001도 500,000보다 작아서 정상적인 길로 인식하는 문제가 발생했다.  
그래서 길의 초기값을 500,001로 설정하여 해결하였다.