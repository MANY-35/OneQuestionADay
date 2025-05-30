# LV3 광고 삽입

### 1차 시도 (실패)
```py
def StrtoSec(s):
    h, m ,s = list(map(int, s.split(":")))
    return ((h*60)+m)*60 + s
def SectoStr(n):
    s, n = n%60, n//60
    m, h = n%60, n//60
    return ":".join([str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)])

def solution(play_time, adv_time, logs):
    play = StrtoSec(play_time)
    abv = StrtoSec(adv_time)
    timeline = [0 for _ in range(play+2)]

    density = [0, play, 0]
    for log in logs:
        s, e = map(StrtoSec, list(log.split('-')))
        timeline[s] += 1
        timeline[e+1] -= 1

    d = [0, len(timeline)]
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]
        if timeline[i] > d[0]:
            d[0], d[1] = timeline[i], i
    l = d[1]
    r = d[1]
    while r-l <= abv:
        if l > 0 and timeline[l-1] >= timeline[r]:
            l-=1
        else:
            r+=1
    return SectoStr(l)
```
누적합 개념을 사용하여 배열로 시간의 밀집도를 구하고 가장 밀집이 높은 점부터 좌우로 펼쳐나가면서 시간을 구하고자 했으나, 절반 이상의 케이스에서 실패했다.  
시간 초과를 예상하였으나 의외로 시간은 오래 걸리지 않았음

*****

### 2차시도 (실패)
```py
def StrtoSec(s):
    h, m ,s = list(map(int, s.split(":")))
    return ((h*60)+m)*60 + s
def SectoStr(n):
    s, n = n%60, n//60
    m, h = n%60, n//60
    return ":".join([str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)])

def solution(play_time, adv_time, logs):
    play = StrtoSec(play_time)
    adv = StrtoSec(adv_time)
    timeline = [0 for _ in range(play+2)]

    first, last = play, 0
    for log in logs:
        s, e = map(StrtoSec, list(log.split('-')))
        timeline[s] += 1
        timeline[e+1] -= 1
        if first > s:
            first = s
        if last < e:
            last = e

    d = [0, len(timeline)]
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]

        if timeline[i] > d[0]:
            d = [timeline[i], i]
    
    print(SectoStr(first), SectoStr(last), SectoStr(d[1]))
    
    if last - first < adv:
        if last - adv < 0:
            return "00:00:00"
        else:
            return SectoStr(last-play)

    l = d[1]
    r = d[1] + adv
    
    if r > play:
        return StrtoSec(play - r)
    
    while l > 0 and timeline[l-1] >= timeline[r]:
        l-=1
        r-=1
    return SectoStr(l)
```
조건을 추가해보앗으나 오히려 더 많은 케이스에서 실패했다.

*****

### 3차 시도(실패)
```py
def StrtoSec(s):
    h, m ,s = list(map(int, s.split(":")))
    return ((h*60)+m)*60 + s
def SectoStr(n):
    s, n = n%60, n//60
    m, h = n%60, n//60
    return ":".join([str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)])

def solution(play_time, adv_time, logs):
    play = StrtoSec(play_time)
    adv = StrtoSec(adv_time)
    timeline = [0 for _ in range(play+2)]
    
    for log in logs:
        s, e = map(StrtoSec, list(log.split('-')))
        timeline[s] += 1
        timeline[e+1] -= 1
        
    s = 0
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]
        
        if len(timeline)-i <= adv:
            s+=timeline[i]

    l, r = play-adv, play
    index = l
    m = s
    while l > 0:
        t = s - timeline[r] + timeline[l-1]
        if t >= m:
            m = t
            index = l-1
        s = t
        l -= 1
        r -= 1
    return SectoStr(index)
```
이전 코드보다 누적합과 슬라이딩 윈도우 방식을 응용하여 맨뒤에서부터 adv_time의 시간만큼을 검사하는 방식으로 코드를 작성하였으나 5개의 케이스에서 실패했다. 예외를 찾아봐야 할 것 같다.

*****

### 4차 시도(성공)
```py
def StrtoSec(s):
    h, m ,s = list(map(int, s.split(":")))
    return ((h*60)+m)*60 + s
def SectoStr(n):
    s, n = n%60, n//60
    m, h = n%60, n//60
    return ":".join([str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)])

def solution(play_time, adv_time, logs):
    play = StrtoSec(play_time)
    adv = StrtoSec(adv_time)
    timeline = [0 for _ in range(play+2)]
    
    for log in logs:
        s, e = map(StrtoSec, list(log.split('-')))
        timeline[s] += 1
        timeline[e] -= 1
    
    s = 0
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]
        if i < play and i >= play-adv:
            s += timeline[i]
            
    l, r = play-adv, play-1
    index = l
    m = s
    while l > 0:
        t = s - timeline[r] + timeline[l-1]
        if t >= m:
            m = t
            index = l-1
        s = t
        l -= 1
        r -= 1

    return SectoStr(index)
```
슬라이딩 윈도우의 범위와 초기 누적합의 설정값에서 문제가 있음을 확인하고 이를 맞게 수정했다.