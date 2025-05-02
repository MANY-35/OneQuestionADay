# LV3 여행 경로

### 1차시도 (실패)
```py
from collections import defaultdict
def solution(tickets):
    info = defaultdict(lambda : [0, 0])
    dc = defaultdict(list)
    for s, e in tickets:
        info[s][0] += 1
        info[e][1] += 1
        dc[s].append(e)
    over = []
    same = []
    for name, c in info.items():
        if c[0] > c[1]:
            over.append(name)
        elif c[0] == c[1]:
            same.append(name)  
    start = sorted(over)
    start.extend(sorted(same))
    start = start[0]
    for n in dc:
        dc[n].sort(reverse=True)
        print(n,dc[n])
    answer = [start]
    while dc[start]:
        dest = dc[start].pop()
        answer.append(dest)
        start = dest
    return answer
```
4분에 1의 데이터 케이스만 통과했다.  
시간만 부족할줄 알았는데 알고리즘 이 잘못된것 같다.

*****

### 2차시도 (실패)
```py
from collections import defaultdict
def solution(tickets):
    info = defaultdict(lambda : [0, 0])
    dc = defaultdict(list)
    for s, e in tickets:
        info[s][0] += 1
        info[e][1] += 1
        dc[s].append(e)
    over = []
    same = []
    for name, c in info.items():
        if c[0] > c[1]:
            over.append(name)
        elif c[0] == c[1]:
            same.append(name)  
    start = sorted(over)
    start.extend(sorted(same))
    start = start[0]
    for n in dc:
        dc[n].sort(reverse=True)

    answer = [start]
    while dc[start]:
        dc[start].sort(key = lambda x:((-info[x][0]), x), reverse=True)
        dest = dc[start].pop()
        info[start][0] -= 1
        info[dest][1] -= 1
        answer.append(dest)
        start = dest
    return answer
```
다음 경로를 선택할때 조건을 추가해보았다. 절반의 케이스에서 실패했다.  
코드를 보다보니 아예 잘못된 방향으로 가고있다는 것을 깨닳았다.

*****

### 3차 시도 (성공)
```py
from collections import defaultdict
import copy
def func(dc:dict, answer:list, now, l, k):
    if len(answer) > l:
        k.append(answer)
        return
    elif dc[now] == []:
        return
    for i in range(len(dc[now])):
        t = answer.copy()
        tdc = copy.deepcopy(dc)
        n = tdc[now].pop(i)
        t.append(n)
        func(tdc, t, n, l, k)

def solution(tickets):
    dc = defaultdict(list)
    for s, e in tickets:
        dc[s].append(e)
    start = 'ICN'
    answer = [start]
    k = []
    func(dc, answer, start, len(tickets), k)
    return sorted(k)[0]
```
이전 코드부터 ICN부터 출발한다는 조건을 보지않고 풀었으며, 완전 탐색이 진행되지 않은 것으로 판단 되어 완전 탐색을 하게끔 코드를 수정 했다.
