# LV2 서버 증설 횟수

### 1차 시도 (성공)
```py
from collections import deque
def solution(players, m, k):
    que = deque()
    n = 0
    count = 0
    for time in range(len(players)):
        if players[time] >= (n+1)*m:
            print(time, players[time], n)
            temp = n
            n = players[time] // m
            temp = n - temp
            count += temp
            que.append((temp, time+k-1))
        if que:
            if que[0][1] == time:
                temp = que.popleft()
                n -= temp[0]
    return count
```
데크를 이용하여 증설 기간이 끝나면 총원을 빼는 식으로 진행했다.