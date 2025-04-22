# LV3 섬 연결하기

#### 1차 시도 (실패)
```py
def solution(n, costs):
    arr = [False for _ in range(n)]
    answer = 0
    for s, e, c in sorted(costs, key=lambda x:x[-1]):
        if arr[s] == True and arr[e] == True:
            continue
        arr[s] = arr[e] = True
        answer += c

        if all(arr):
            return answer
    return answer
```
> 두개의 케이스만 통과했다. 알고리즘이 틀린것 같다. 가장 작은 길부터 연결하는 방식을 택했는데 고려하지 않은 것이 있는것 같다.

*****

### 2차 시도 (성공)
```py
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
def solution(n, costs):
    answer = 0
    table = [i for i in range(n)]
    for s,e,c in sorted(costs, key=lambda x:(x[-1],x[0])):
        if find(table, s) != find(table, e):
            union(table, s, e)
            answer += c
    return answer
```
> union-find 알고리즘이라는 것을 찾아서 적용시켜 풀었다.
