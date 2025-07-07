# LV2 점 찍기기

### 1차시도 (성공공)
```py
import math

def solution(k, d):
    answer = 0
    for y in range(0, d+1, k):
        answer += int(math.sqrt(d**2 - y**2))//k + 1
    return answer
```

y좌표를 고정한 상태로 최대 x 값을 구하고, 최대 x값 까지 가능한 x좌표의 갯수를 구하는 방식으로 접근했다.

*****

