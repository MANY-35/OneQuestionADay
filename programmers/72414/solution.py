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
    # for i in range(adv):
    #     s+=timeline[l+i]
        
    print(s)
    
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


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))

#7 8 11 12 18 24

