# LV2 완전범죄

### 1차 시도 (실패)
```py
def solution(info, n, m):
    arr = sorted(info, key=lambda x : (x[0], -x[1]), reverse=True)
    sum = [0, 0]
    for k in arr:
        if sum[1] + k[1] < m:
            sum[1] += k[1]
        else:
            sum[0] += k[0]
    if sum[0] >= n:
        return -1
    return sum[0]
```
두 개의 테스트 케이스에서 실패했다.  
완전 탐색을 진행하지 않고 풀어보고 싶었으나 불가능할지도 모르겠다.

*****

### 2차 시도 (실패)
```py
def solution(info, n, m):
    answer = []
    inf = sum([x[0] for x in info])
    
    c = pow(2,len(info))
    for i in range(c):
        arr = [inf, 0]
        j = 0
        t = i
        while t:
            if t%2:
                arr[0] -= info[j][0]
                arr[1] += info[j][1]
            t//=2
            j+=1
        answer.append(arr)
    answer = sorted(answer, key=lambda x:x[0])
    for a in answer:
        if a[0] < n and a[1] < m:
            return a[0]
    return -1
```
모든 경우의 수를 탐색하는 방식으로 진행해보았으나 시간이 너무 오래 걸린다.

*****

### 3차 시도 (성공)
```py
def solution(info, n, m):
    answer = 0
    info = sorted(info, key=lambda x: (x[1]-x[0]))
    sum = 0
    for data in info:
        if sum + data[1] < m:
            sum += data[1]
        else:
            answer += data[0]
    if answer >= n:
        return -1
    return answer
```
완전 탐색은 불가능하다고 판단하여 탐욕법의 느낌으로 풀어보고자 했고, B 도둑이 최대한 많이 가져갈 수 있는 방법을 고민했다.
