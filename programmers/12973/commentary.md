# LV2 짝지어 제거하기

### 1차 시도 (성공)
```py
def solution(s):
    stack = ['']

    for i in s:
        a = stack.pop()
        if a == i:
            continue
        stack.append(a)
        stack.append(i)

    if len(stack) > 1:
        return 0
    return 1
```
> 현재 문자열의 마지막 문자와 같은 문자가 나오면 제거하면서 모든 문자열에서의 짝을 제거한다.