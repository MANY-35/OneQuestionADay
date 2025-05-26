# LV2 두 원 사이의 정수 쌍

### 1차시도 (실패)
```py
import math
def f(r):
    count = r
    for i in range(1, r):
        count += int(math.sqrt(r**2 - i**2))
    return count * 4 + 1
    
def solution(r1, r2):    
    r1 = f(r1)
    r2 = f(r2)
    return r2-r1+4
```
원의 부채꼴에 대하여 x 좌표별 y의 최대 값을 구하여 더하고 X4 를 진행하여 원 내부의 정점의 갯수를 구하는 함수를 작성하고,  
두 원에 대하여 큰 원의 정점의 갯수에서 작은 원의 정점의 갯수의 차를 구하는 방식으로 접근했다.  
하지만 절반 보다 많은 케이스에서 실패했다.  
원 내부의 정점의 갯수를 구하는 방식에 문제가 있는 것으로 추측된다.

-----

### 2차시도 (성공)
```py
import math
def f(r):
    count = r
    for i in range(1, r):
        count += math.floor(math.sqrt(r**2 - i**2))
    return count * 4 + 1
def solution(r1, r2):
    c = 0
    for i in range(0, r1):
        k = math.sqrt(r1**2 - i**2)
        if k == math.floor(k):
            c += 1
    c *= 4
    return f(r2) - f(r1) + c
```

이전 코드에서 작은 원 위의 점을 계산할 때 단순히 x가 0 일때 두개, y가 0 일때 두개라는 잘못된 판단을 해서 실패했다는 것을 알았다.  
그래서 작은원 위의 점들의 갯수를 구하는 식을 통해 이를 해결했다.