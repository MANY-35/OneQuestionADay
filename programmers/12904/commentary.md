# LV3 가장 긴 팰린드롬

### 1차 시도 (실패)
```py
def check(s, l, r):
    for i in range(1, (r-l+1)//2):
        if s[l+i] != s[r-i]:
            return False
    return True
def solution(s):
    answer = 0
    for l in range(len(s)):
        for r in range(len(s)-1, l-1, -1):
            if s[l] == s[r]:
                break
        if check(s, l, r):
            answer = max(answer, (r-l+1))
    return answer
```
시작점부터 한 문자씩 움직이고 끝부터 한 문자씩 움직이면서 팰린드롬인지 판단하는 코드를 작성해봤는데, 3분의 2의 케이스에서 실패했습니다.  
알고리즘상 문제가 있는 것으로 판단됩니다.

*****

### 2차 시도 (실패)
```py
def check(s, l, r):
    for i in range(1, (r-l+1)//2+1):
        if s[l+i] != s[r-i]:
            return False
    return True
def solution(s):
    answer = 0
    for l in range(len(s)):
        for r in range(len(s)-1, l-1, -1):
            if s[l] == s[r]:
                if check(s, l, r):
                    answer = max(answer, (r-l+1))
    return answer
```
이전 코드에서 끝 위치를 한 번만 설정하는 오류가 있는 것을 발견하여 코드를 수정했습니다.  
효율성 부분에서 한 개의 케이스에서 시간 초과가 발생했습니다.

*****

### 3차 시도 (성공)
```py
def check(s, l, r):
    for i in range(1, (r-l+1)//2+1):
        if s[l+i] != s[r-i]:
            return False
    return True
def solution(s):
    answer = 0
    for l in range(len(s)):
        for r in range(len(s)-1, l-1, -1):
            if s[l] == s[r] and answer < (r-l+1):
                if check(s, l, r):
                    answer = r-l+1
    return answer
```
이전 코드에서 check 함수로 팰린드롬을 확인한 후 그 길이를 저장하는 방식에서, 길이가 원래 있던 것보다 긴 문자열에 대해서만 검사를 진행하는 방식으로 시간을 단축했습니다.
