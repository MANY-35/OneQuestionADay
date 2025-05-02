# LV3 숫자 게임

#### 1차 시도 (실패)
```py
def solution(A, B):
    A = sorted(A)
    B = sorted(B)

    c = 0
    for a in A:
        for i in range(len(B)):
            if a < B[i]:
                c += 1
                t = B[i]
                B[i] = B[0]
                B[0] = t
                break
        B = B[1:]
    return c
```
효율성 부분에서 실패가 발생했다.  
배열을 제거하면서 계산하여 시간을 줄여보려 했지만 부족했던 것 같다.

*****

### 2차 시도 (실패)
```py
def search(arr, target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left < len(arr):
        return left
    return 0

def solution(A, B):
    A = sorted(A)
    B = sorted(B)
    c = 0
    for a in A:
        s = search(B, a)
        if a < B[s]:
            c += 1
        B = B[:s] + B[s+1:]
    return c
```
이진 탐색으로 시간을 줄여보려 했지만 마찬가지로 시간 초과가 발생했다.

*****

### 3차 시도 (성공)
```py
def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    answer = 0
    while B:
        if A[-1] < B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            B.pop()
    return answer
```
탐색 과정을 줄여서 시간을 단축했다.