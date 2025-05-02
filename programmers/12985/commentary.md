# LV2 예상 대진표

### 1차 시도 (성공)
```py
def solution(n,a,b):
    i = 0
    while(a != b):
        i += 1
        if a > 1:
            a = a//2 + a%2
        if b > 1:
            b = b//2 + b%2
    return i
```
토너먼트가 1부터 순차대로 진행되기 때문에 a와 b의 순서를 매 회 수정하면서 같아질 때까지 반복하여 풀었다.