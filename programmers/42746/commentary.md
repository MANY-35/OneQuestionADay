# LV3 가장 긴 팰린드롬

### 1차시도 (실패)
```py
from functools import cmp_to_key
def strCmp(s1, s2):
    t1 = str(s1)
    t2 = str(s2)
    t1 = t1.ljust(4, t1[-1])
    t2 = t2.ljust(4, t2[-1])
    if int(t1) > int(t2):
        return -1
    return 1

def solution(numbers):
    answer = ''
    s = sorted(numbers, key=cmp_to_key(strCmp))
    for i in s:
        answer += str(i)
    return answer
```
단순하게 모든 원소의 값이 1000이하 이기 때문에 각 원소를 문자로 치환하여 마지막 숫자를 반복하여 채워넣은 후 값을 비교하면 될 것 같다는 생각으로 작성하였으나 실패 했다.

*****

### 2차시도 (실패)
```py
from functools import cmp_to_key
def strCmp(s1, s2):
    flag = 0
    t1 = str(s1)
    t2 = str(s2)
    if len(t1) > len(t2):
        t2 = t2.ljust(len(t1), t2[-1])
        flag = 1
    else :
        t1 = t1.ljust(len(t2), t1[-1])
        flag = -1
    if int(t1) == int(t2):
        return flag
    if int(t1) > int(t2):
        return -1
    return 1

def solution(numbers):
    answer = ''
    s = sorted(numbers, key=cmp_to_key(strCmp))
    for i in s:
        answer += str(i)
    return answer
```
이전 코드에서 반례를 발견하여 이번엔 비교하는 대상의 길이만큼만 채워 넣은 후 비교하면 될 것 같아서 수정해 보았으나 실패했다.

*****

### 3차시도 (성공)
```py
from functools import cmp_to_key
def strCmp(s1, s2):
    t1 = str(s1)
    t2 = str(s2)
    if len(t1) != len(t2):
        temp = t1
        t1 += t2
        t2 += temp
    if int(t1) > int(t2):
        return -1
    return 1

def solution(numbers):
    answer = ''
    s = sorted(numbers, key=cmp_to_key(strCmp))
    if s[0] == 0:
        return '0'
    for i in s:
        answer += str(i)
    return answer
```
이전 코드에서 반례를 찾을 수 없어서 고민하다가 다른사람들의 질문을 참고하여 테스트 케이스를 알아 보았다.  
우선 0이 n 개 있는 배열은 0*n 이 아니라 0으로 만들어야 한다는 이상한 케이스가 존재했다. 또한 두 수를 비교 할때 더해서 비교하는 것이 정답이 였다는 것을 알 수 있었다.
