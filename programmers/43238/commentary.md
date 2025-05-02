# LV3 입국심사

### 1차시도 (실패)
```py
import heapq
def solution(n, times):
    times = [(t, t) for t in times]
    heapq.heapify(times)
    for i in range(n):
        d, n = heapq.heappop(times)
        heapq.heappush(times, (d+n, n))
    return d
```
단순하게 생각해서 대기큐를 만들고 그 심사를 시작한 심사대의 다음 입장 가능 시간을 저장하여 가장 작은 칸부터 심사를 받도록 했다.  
시간복잡도 상으로 O(nlog n)이라고 생각했는데 n이 10억이라는 큰 수여서 그런지 4개의 케이스에서 시간초과가 발생했다.

*****

### 2차시도 (성공)
```py
def check(times, m, n):
    return n <= sum([m//i for i in times])
def solution(n, times):
    l, r = 0, max(times) * n
    while l < r:
        m = (l+r)//2
        l, r = (l, m) if check(times, m, n) else (m+1, r)
    return l
```
인원수를 기준으로 판단하게 되면 아무리 빨라도 O(nlog n)이상의 속도로 구하는 방법이 도저히 떠오르지 않아 검색을 통해 시간을 기준으로 이분 탐색을 하는 경우 O(log n)으로 줄일 수 있다는 것을 알았다.