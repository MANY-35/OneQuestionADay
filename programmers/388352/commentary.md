# LV2 비밀 코드 해독

### 1차 시도 (실패)
```py
from itertools import combinations
from collections import deque

def solution(n, q, ans):
    answer = 0
    possible = [True for _ in range(n)]

    que = deque(sorted(zip(q, ans), key=lambda x: x[1]))
    l = que.pop()
    if l[0] == 5:
        return 1
    
    que.append(l)
    while que[0][1] == 0:
        for i in que.popleft()[0]:
            possible[i-1] = False
    
    temp = []
    for i in range(n):
        if possible[i] and i+1 not in l[0]:
            temp.append(i+1)
    
    arr = []
    for t in list(combinations(temp, 5-l[1])):
        for a in list(combinations(l[0], l[1])):
            arr.append(t + a)
            
    for a in arr:
        for i in que:
            t = 0
            for j in i[0]:
                if j in a:
                    t += 1
            if t != i[1]:
                break
        if t == i[1]:
            answer += 1
    return answer
```
절반 정도의 케이스에서 실패했다.  
완전 탐색으로 모든 조합을 확인할 경우 n이 최대 30이기 때문에  
30 C 5로 15만 이상의 결과가 나오기 때문에 이를 m의 최대 10만큼 반복하면 150만이라는 값이 나오기에 결과에서 0이 나오는 케이스들의 수는 배제하여 풀고자 했다.

*****

### 2차 시도 (성공)
```py
from itertools import combinations
def solution(n, q, ans):
    answer = 0
    possible = [True for _ in range(n)]

    que = list(sorted(zip(q, ans), key=lambda x: x[1]))
    l = que.pop()
    if l[0] == 5:
        return 1
    
    que.append(l)
    for i in que:
        if i[1] == 0:
            for j in i[0]:
                possible[j-1] = False
    
    temp = []
    for i in range(n):
        if possible[i] and i+1 not in l[0]:
            temp.append(i+1)

    arr = []
    for t in list(combinations(temp, 5-l[1])):
        for a in list(combinations(l[0], l[1])):
            arr.append(t + a)

    for a in arr:
        l = 0
        for k in que:
            t = 0
            for j in k[0]:
                if j in a:
                    t += 1
            if t != k[1]:
                break
            l += 1
        if l == len(que):
            answer += 1
    return answer
```
처음 생각했을 때는 결과가 0인 값들을 모두 배제하고 풀었으나 이 생각이 잘못되었다는 것을 알게 되었다.  
후에 경우의 수를 계산할 때 0인 것 또한 고려를 해야 정확한 결과가 나오는 것이다.
>p.s.  
다른 사람의 풀이를 보니 모든 경우를 탐색하는 완전 탐색으로 풀어도 생각보다 오랜 시간이 걸리지 않는 것을 알 수 있었고, set 자료형의 & 연산자를 통해 교집합을 간단하게 구할 수 있다는 것을 알게 되었다.
