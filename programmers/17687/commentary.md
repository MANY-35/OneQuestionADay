# LV2 [3차] n진수 게임

### 1차 시도 (실패)
```py
def solution(n, t, m, p):
    modle = {2: lambda x : list(bin(x)[2:]), 10:str, 16: lambda x : list(hex(x)[2:])}
    n = modle[n]

    arr = []
    num = 0
    x = i = 1
    while t > len(arr) :
        target = n(num)
        for j in target:
            if i == p + (x-1)*m:
                arr.append(j)
                x += 1
            i += 1 
        num += 1

    answer = ''
    for i in range(t):
        answer += arr[i].upper()
    return answer
```
> 몇몇 케이스에서 런타임 에러가 발생했습니다. 처음 문제를 봤을 때 2, 10, 16진수만 사용할 것이라고 착각했는데, 문제를 다시 보니 2~16 진법으로 문제를 풀어야 했습니다.

*****

### 2차 시도 (성공)
```py
def f(x, y):
    code = "0123456789ABCDEF"
    t = []
    while x > 0:
        t.append(code[x%y])
        x //= y
    if t == []:
        return ['0']
    t.reverse()
    return t

def solution(n, t, m, p):
    arr = []
    num = 0
    x = i = 1
    while t > len(arr) :
        target = f(num, n)
        for j in target:
            if i == p + (x-1)*m:
                arr.append(j)
                x += 1
            i += 1 
        num += 1

    answer = ''
    for i in range(t):
        answer += arr[i]
    return answer
```
> 다른 사람들의 풀이를 보니 파이썬의 다양한 문법과 기능을 더 공부해야 할 것 같습니다. 특히 진법 변환에 대한 내장 함수나 더 효율적인 방법이 있을 것 같습니다.

### 문제 해결 과정
1. 첫 번째 시도에서는 2, 10, 16진수만을 고려한 딕셔너리를 사용했으나, 이는 문제의 요구사항(2~16진법)을 충족시키지 못했습니다.
2. 두 번째 시도에서는 직접 진법 변환 함수 `f()`를 구현하여 모든 진법에 대응할 수 있도록 했습니다.
3. 진법 변환 시 0~F까지의 숫자를 표현하기 위해 문자열 "0123456789ABCDEF"를 활용했습니다.
4. 결과적으로 모든 테스트 케이스를 통과할 수 있었습니다.
