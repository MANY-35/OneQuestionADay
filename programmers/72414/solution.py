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