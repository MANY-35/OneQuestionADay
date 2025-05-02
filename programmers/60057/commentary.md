# LV2 튜플

### 1차시도 (실패)
```py
def solution(s):
    m = []
    for l in range(1, len(s)//2+1):
        t = []
        for i in range(0,len(s)-l+1, l):
            t.append(s[i:i+l])
        t.append(s[i+l:])

        c = 0
        k = ""
        for i in range(0, len(t)-1):
            if t[i] == t[i+1]:
                c += 1
            else:
                k += str(c+1) + t[i]
                c = 0
        k = k.replace('1', "") + t[-1]
        m.append(len(k))
    return min(m)
```
몇몇 케이스에서 실패했으며 런타임 에러가 발생한 케이스가 존재하는 것으로 보아 짧은 문자열에서의 문제가 발생하는 것으로 사료된다.

*****

### 2차시도 (실패)
```py
def solution(s):
    m = []
    for l in range(1, len(s)//2+1):
        t = []
        for i in range(0,len(s)-l+1, l):
            t.append(s[i:i+l])
        t.append(s[i+l:])

        c = 0
        k = ""
        for i in range(0, len(t)-1):
            if t[i] == t[i+1]:
                c += 1
            else:
                if c>0:
                    k += str(c+1) + t[i]
                else:
                    k+= t[i]
                c = 0
        k += t[-1]
        m.append(len(k))
    return sorted(m)[0]
```
하나의 데이터 케이스에서 런타임 에러가 발생하며 그 외에는 모두 통과했다.  
이전 코드에서 m배열이 비어있는 경우가 발생하여 에러가 발생한다고 생각했으나 아니였음

*****

### 3차시도 (성공)
```py
def solution(s):
    m = []
    for l in range(1, len(s)+1):
        t = []
        for i in range(0,len(s)-l+1, l):
            t.append(s[i:i+l])
        t.append(s[i+l:])

        c = 0
        k = ""
        for i in range(0, len(t)-1):
            if t[i] == t[i+1]:
                c += 1
            else:
                if c>0:
                    k += str(c+1) + t[i]
                else:
                    k+= t[i]
                c = 0
        k += t[-1]
        m.append(len(k))
    return sorted(m)[0]
```
문자열이 한개일때 반복문이 돌아가지 않아서 발생한 문제였다.