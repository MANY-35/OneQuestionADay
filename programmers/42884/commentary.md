# LV3 단속카메라

### 1차시도 (실패)
```py
def solution(routes):
    routes = sorted(routes, key=lambda x:(x[1]-x[0]))
    c = 0
    while routes:
        l = routes[0][0]
        r = routes[0][1]
        t = []
        for route in routes:
            if l <= route[0] and route[0] <= r:
                l = route[0]
            if l <= route[1] and route[1] <= r:
                r = route[1]

            if r < route[0] or l > route[1]:
                t.append(route)
        routes = t
        c += 1
    return c
```
> 효율성 테스트 부분에서 2개의 실패가 나왔다. 시간초과가 아니라 실패가 나온것으로 보아 코드에 잘못된 부분이 있는것 같다.

*****

### 2차시도 (성공)
```py
def solution(routes):
    routes = sorted(routes, key=lambda x:x[1])
    c = 0
    while routes:
        t = []
        for route in routes:
            if route[0] > routes[0][1]:
                t.append(route)
        c += 1
        routes = t
    return c
```
> 알고리즘 적으로 잘못됐음을 깨닫고 코드를 수정함