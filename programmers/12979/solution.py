def solution(n, stations, w):
    temp = []
    t = 0
    for s in stations:
        temp.append(s-w-t-1)
        t = s+w
    temp.append(n-t)
    temp = [i for i in temp if i>0]

    answer = 0
    k = w*2+1
    for t in temp:
        answer += t // k
        if t%k > 0:
            answer += 1

    return answer