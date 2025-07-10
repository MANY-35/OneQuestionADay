# LV2 우박수열 정적분

### 1차시도 (실패)
```py
def solution(k, ranges):
    answer = []

    sumArr = [0]
    be = k
    count = 0
    while be != 1:
        if be % 2 == 0:
            n = be // 2
        else:
            n = be * 3 + 1
            
        if n < be:
            area = be - (be-n)/2
        else:
            area = be + (n-be)/2
        sumArr.append(sumArr[-1] + area)
        be = n
        count += 1
        
    for a, b in ranges:
        if b < 0:
            b = count + b
        if a > b:
            answer.append(-1.0)
        elif a == 0 and b == 0:
            answer.append(sumArr[-1])
        else:
            answer.append(sumArr[b] - sumArr[a])
    return answer
```

정적분이라는 말에 속아 정적분을 구하려다가 우박수열이 실수에 대해서 정의가 가능한지 의문이기에 정적분을 구하는 것이 문제가 아니라는 것을 깨닫고 정수에 대해서는 그래프들이 x에 대해서 1씩 증가할 떄, 삼각형과 사각형의 합으로 나타 낼 수 있다는 것을 알아냈고, 문제에서 구간의 넓이를 구하는 것이기 때문에 누적합을 통해 계산을 빠르게 할 수 있을 것이라고 생각하고 접근했다.  
어찌된 영문인지 예제는 맞았으나 다른 테스트케이스에서 모두 실패했다.

*****

### 2차시도 (성공)
```py
def solution(k, ranges):
    answer = []

    sumArr = [0]
    be = k
    while be != 1:
        if be % 2 == 0:
            n = be // 2
        else:
            n = be * 3 + 1
            
        if n < be:
            area = n + (be-n)/2
        else:
            area = be + (n-be)/2
        sumArr.append(sumArr[-1] + area)
        be = n
    for a, b in ranges:
        b = len(sumArr)-1 + b
        if a > b:
            answer.append(-1.0)
        else:
            answer.append(sumArr[b] - sumArr[a])
    return answer
```
문제의 조건을 잘 못 이해해서 생긴 문제였다.  
> 0 이상의 수 b에 대해 [a, -b]에 대한 정적분 결과는 x = a, x = n - b, y = 0 으로 둘러 쌓인 공간의 면적으로 정의하며

해당 정의와 b의 범위가 
> ranges의 원소는 [a, b] 형식이며 0 ≤ a < 200, -200 < b ≤ 0 입니다.

이므로 모든 b에 대해 n - b 로 정의를 했어야 하는 문제였다. 따라서 a, b가 0일때 와 b만 0일 때의 조건을 다르게 설정해야 한다는 것을 알아냈다.

*****