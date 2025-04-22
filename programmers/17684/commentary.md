# LV2 [3차] 압축

### 1차 시도 (실패)
```py
def solution(msg):
    dictionary = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = []
    i=0
    while i < len(msg):
        w = msg[i:]
        while w not in dictionary:
            c = w[-1]
            w = w[:-1]

        answer.append(dictionary.index(w)+1)
        dictionary.append(w+c)
        i += len(w)
    return answer
```
> 9번 데이터 케이스만 런타임 오류가 발생했다. 감을 찾지 못해서 데이터 케이스를 찾아보니 'A'가 들어온 경우였고, 작성한 코드에서 내부 반복문을 진행하지 않기 때문에 c가 생성되지 못해 생긴 문제였다.

*****

### 2차 시도 (성공)
```py
def solution(msg):
    dictionary = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = []
    i= 0
    while i < len(msg):
        w = c = msg[i:]
        while w not in dictionary:
            c = w[-1]
            w = w[:-1]

        answer.append(dictionary.index(w)+1)
        dictionary.append(w+c)
        i += len(w)
    return answer
```
> 간단하게 c를 초기화해 주어서 해결했다.