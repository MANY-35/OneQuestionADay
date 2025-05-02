# LV3 최고의 집합

### 1차 시도 (성공)
```py
def solution(n, s):
    arr = [s//n for _ in range(n)]

    for i in range(1, s - sum(arr)+1):
        arr[-i] += 1
    
    if 0 in arr:
        return [-1]
    return arr
```
처음에는 조합을 이용하여 모든 배열을 구성한 뒤 검색하며 찾아보려 했으나, 아무리 봐도 오래 걸릴 것 같아 다른 방법을 찾던 중 곱의 최댓값이 되는 수열은 모든 값이 비슷한 수들일 것 같아 그렇게 접근해보았더니 맞았다.