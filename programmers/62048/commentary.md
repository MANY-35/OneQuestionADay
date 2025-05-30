# LV2 튜플

### 1차시도 (실패)
```py
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    arr = set()
    for x in range(0, X):
        y = (Y/X) * x
        y = int(y * 10) / 10
        arr.add((x, y))

    for y in range(0, Y):
        x = (X/Y)*y
        x = int(x * 10) / 10
        arr.add((x, y))
        
    return X*Y - len(arr)
```
하나의 데이터 케이스를 실패하였으며 절반의 케이스에서 시간 초과가 발생했다.  
원점을 지나고 w,h 좌표를 지나는 직선의 그래프로 생각하여 x값과 y값을 구해서 저장하는 방식으로 풀어봤다.

*****

### 2차시도 (실패)
```py
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    
    for x in range(1,X):
        y = (Y/X) * x
        if int(y * 100)/10 % 10 == 0:
            break
    X, Y, C= x, int(Y/(X/x)), X/x
    
    arr = set()
    for x in range(0, X):
        y = (Y/X) * x
        y = int(y * 10) / 10
        arr.add((x, y))

    for y in range(0, Y):
        x = (X/Y)*y
        x = int(x * 10) / 10
        arr.add((x, y))
    
    return int(w*h - (len(arr)*C))
```
X, Y의 값을 처음부터 끝까지 하는 것이 아니라 같은 패턴의 반복으로 가정하고 하나의 패턴을 분석하여 곱하는 식으로 변경했다.  
시간이 초과하지는 않았지만 여전히 절반의 케이스에서 실패했다.

*****

### 3차시도 (실패)
```py
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    def gcd(x, y):
        while y:
            x, y = y, x%y
        return x
    C = gcd(X,Y)
    X, Y = int(X/C), int(Y/C)
    
    c = 1
    for x in range(X-1):
        y = set()
        y.add(((Y/X)*x)//1)
        y.add(((Y/X)*(x+1))//1)
        c += len(y)
    return int(w*h - (c*C))
```
시간초과가 발생했다.

*****

### 4차시도 (실패)
```py
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    c, x, a = 1, 0, Y/X
    while x<X:
        y = a*(x+1)
        if x != 0 and y%1 == 0:
            break
        y = set()
        y.add((a*x)//1)
        y.add((a*(x+1))//1)
        c += len(y)
        x+=1
    x+=1
    return int(w*h - (c * X/x))
```
시간을 최대한 줄여보려고 노력했지만 여전히 시간이 초과하는 케이스가 존재하며, 실패한 케이스도 존재했다.

*****

### 5차시도 (실패)
```py
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    c, x, a = 1, 1, Y/X
    y_ = 0
    while x<X:
        y = a*x
        if y%1 == 0:
            break
        c += 1 + (y//1 - y_//1)
        y_ = y
        x+=1
    return int(w*h - (c * X/x))
```
4개의 케이스에서 시간초과가 발생했다.

*****

### 5차시도 (성공)
```py
def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    C = gcd(X, Y)
    X, Y =X//C, Y//C
    
    if X==Y:
        c = X
    else:
        c = X+Y-1
    return int(w*h - (C*c))
```