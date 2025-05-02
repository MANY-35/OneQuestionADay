# LV2 오픈 채팅방

### 1차시도 (실패)
```py
def check(record):
    if record == "":
        return False
    if record[0] == ")" or record[-1] == "(":
        return False
    f = j = 0
    for j in record:
        if j == "(":
            f += 1
        else:
            f -= 1
        
        if f < 0:
            return False
    return True
    
def solution(record):
    if check(record):
        return record
    
    o = c = i = 0    
    u = v = ""
    for i in range(len(record)):
        if record[i] == "(":
            o += 1
        else:
            c += 1
        if o == c:
            break
    u = record[:i+1]
    v = record[i+1:]

    if check(u):
        return u + solution(v)
    else:
        t = ['(' if u[i]==")" else ')' for i in range(len(u))]
        u = "("+"".join(t[1:-1])+")"
        
        return u + v
```
절반 이상의 케이스에 대해 실패했다.   
다시 생각해 보니 문자열을 만드는게 이상한것 같다.

*****

### 2차시도 (실패)
```py
def check(record):
    if record == "":
        return False
    if record[0] == ")" or record[-1] == "(":
        return False
    f = j = 0
    for j in record:
        if j == "(":
            f += 1
        else:
            f -= 1
        
        if f < 0:
            return False
    return True
    
def solution(record):
    if check(record):
        return record
    
    o = c = i = 0    
    u = v = ""
    for i in range(len(record)):
        if record[i] == "(":
            o += 1
        else:
            c += 1
        if o == c:
            break
    u = record[:i+1]
    v = record[i+1:]
    
    if not check(u):
        t = ['(' if u[i]==")" else ')' for i in range(len(u))]
        u = "("+"".join(t[1:-1])+")"
    
    if v == "":
        return u
    return u + solution(v)
```
이전 코드와 마찬가지로 대부분의 케이스에 실패했다.

*****

### 3차시도 (성공)
```py
def check(record):
    f = 0
    for j in record:
        if j == "(":
            f += 1
        else:
            f -= 1
        if f < 0:
            return False
    return True

def solution(record):
    if record == "":
        return ""
    
    o = c = 0    
    u = v = ""
    for i in range(len(record)):
        if record[i] == "(":
            o += 1
        else:
            c += 1
        if o == c:
            break
    u = record[:i+1]
    v = record[i+1:]
    
    if check(u):
        return u + solution(v)
    k = "(" + solution(v) + ")"
    u = k + "".join(['(' if u[i]==")" else ')' for i in range(1, len(u)-1)])
    return u
```
문제를 다시 읽고보니 이전 코드들은 주어진 조건대로 수행하지 않고 내 마음대로 문제를 재해석 했었던 것이 문제였다.