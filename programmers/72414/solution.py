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


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))