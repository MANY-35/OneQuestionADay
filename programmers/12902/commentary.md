# LV2 3 X n 타일링

## 1차 시도 (성공)
```python
def solution(n):
    if n==2:
        return 3
    if n==4:
        return 11
    answer = 0
    n/=2
    n-=2
    c=(3,11)
    while n>0:
        c=(c[1],c[1]*4-c[0])
        n-=1
    return c[1]%1000000007
```
해법이 도저히 떠오르지 않아 검색해 보니 알고리즘적인 문제라기보다는 단순한 점화식을 도출하여 푸는 방식이었다.
