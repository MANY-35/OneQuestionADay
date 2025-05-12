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

