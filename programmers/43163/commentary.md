# LV3 단어 변환

### 1차시도 (실패)
```py
def solution(begin, target, words):
    def checker(str1, str2):
        s = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        d = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in str1:
            d[i] += 1
        for i in str2:
            s[i] += 1
        c = 0
        for i, j in zip(s.values(), d.values()):
            if i != j:
                c+=1
        if c > 2:
            return False
        return True
    
    que = [begin]
    visted = []
    c = 0
    while que:
        t = que.pop()
        c += 1
        for i in words:
            if i not in visted and checker(t, i):
                if i == target:
                    return c
                else:
                    que.append(i)
                    visted.append(i)
    return 0
```
> 하나의 데이터케이스를 실패했다. 한글자만 다른지 확인하는 함수가 잘못된것 같다.

*****

### 2차시도 (성공)
```py
def checker(str1, str2):
    c = 0
    for i, j in zip(str1, str2):
        if i != j:
            c+=1
    if c > 1:
        return False
    return True

def solution(begin, target, words):
    que = [begin]
    visted = []
    
    c = 0
    while que:
        t = que.pop()
        c += 1
        for i in words:
            if i not in visted and checker(t, i):
                if i == target:
                    return c
                else:
                    que.append(i)
                    visted.append(i)
    return 0
```
> 단어를 비교하는 함수를 너무 힘들게 생각했던 것 같다.