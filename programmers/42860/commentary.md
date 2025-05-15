# LV2 조이스틱

### 1차시도 (실패)
```py
def displacement(ch):
    t, ch = ord('Z')+1 - ord('A'), ord(ch)-ord('A')
    if t - ch < ch:
        return t - ch
    return ch
    
def solution(name):
    answer = 0
    for ch in name:
        answer += displacement(ch)
    answer += len(name) - 1
    if name[1] == 'A' or name[-1] == 'A':
        answer -= 1
    return answer
```

단순하게 생각하여 해당 위치에서 역순으로 가는것이 빠른지 정순으로 가는게 빠른지 계산하는 함수를 작성하고  
그 값을 전부 저장한 후 왼쪽으로 갈지 오른쪽으로 갈지 정하는 방식으로 접근 하였으나  
절반이상의 케이스에서 실패했고, 런타임 에러가 발생한 케이스가 존재한다.  
다시 살펴보니 name의 길이가 1~ 이기 때문에 문자열이 한글자 일때 name[1] 로 접근하는 문제가 발생하는 것을 알았고,   
왼쪽과 오른쪽으로 움직이는 방향을 정할때 단순히 첫위치에서 왼쪽 오른쪽을 정하면 된다고 생각하는 것이 틀렸다.

-----

### 2차시도 (실패)
```py
def howLong(ch):
    t, ch = ord('Z')+1 - ord('A'), ord(ch)-ord('A')
    if t - ch < ch:
        return t - ch
    return ch

def solution(name):
    answer = 0
    conti = 0
    max = 0
    for ch in name:
        if ch == 'A':
            conti += 1
            continue
        if max < conti:
            max = conti
            conti = 0
        answer += howLong(ch)
    answer += len(name) - 1 - max
    return answer
```

연속적인 A가 가장 많은 구간을 지나지 않는 것이 방법이라고 생각한것이 틀린것같다.

-----

### 3차시도 (실패)
```py
def displacement(ch):
    t, ch = ord('Z')+1 - ord('A') , ord(ch) - ord('A')
    if t - ch < ch:
        return t - ch
    return ch
    
def solution(name):
    answer = 0
    flag = True
    name = list(name)
    for i in range(len(name)):
        if name[i] == 'A':
            flag = False
            name[i] = 0
            continue
        answer += displacement(name[i])
        name[i] = 1
    
    if flag:
        return answer + len(name) - 1
    d = 0
    j = 0
    while True:
        d += 1
        if (j+d)%len(name) == j:
            break
        if name[(j+d)%len(name)] ^ name[(j-d)%len(name)] == 0:
            continue
        answer += d
        if name[(j+d)%len(name)]:
            for i in range(d+1):
                name[(j+i)%len(name)] = 0
            j = (j+d)%len(name)
        else:
            for i in range(d+1):
                name[(j-i)%len(name)] = 0
            j = (j-d)%len(name)
        d = 0
    return answer
```

문자 A를 0으로 그 외에는 1로 치완하여 XOR 연산자를 이용해 둘중 하나가 A가 아닐 때 를 판단하여 계산하는 식으로 접근해 보았다.  
하지만 여전히 1/3 정도의 케이스에서 실패 했다.  
아무리 고민해 보아도 탐욕법으로 푸는 방법을 찾지 못하겠다.

-----

### 4차시도 (성공)
```py
def displacement(ch):
    t, ch = ord('Z')+1 - ord('A') , ord(ch) - ord('A')
    if t - ch < ch:
        return t - ch
    return ch

def solution(name):
    answer = 0
    minPath = len(name) - 1
    
    for i in range(len(name)):
        answer += displacement(name[i])
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        if next - i > 1:    
            minPath = min(minPath, i*2 + len(name) - next)
            minPath = min(minPath, (len(name) - next)*2 + i)
    return answer + minPath
```

도저히 풀리지 않아서 찾아보았다. 너무 어렵게 접근한 것이 문제였다.  
문제의 본질은 어차피 모든 구역을 탐사하는데, 딱 하나의 연결된 A들의 집합만 지나지 않는다는 점이다.  
기본적으로 모든 글자를 만나는 것이 최소의 움직임이라고 판단하고,  
현재 만난 A의 집합을 건널 때의 움직임 횟수와 건너지 않을 때의 움직임 횟수 중 가장 작은 값을 찾으면 된다.  
이 과정을 만나는 모든 A의 집합에서 계산해 주는 것이 방법이다.

-----