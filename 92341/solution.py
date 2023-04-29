def solution(fees, records):
    def subTime(a, b):
        a = [int(i) for i in a.split(":")]
        b = [int(i) for i in b.split(":")]
        a = a[0]*60 + a[1]
        b = b[0]*60 + b[1]
        return a-b


    cal = {r.split(" ")[1]:[] for r in records}
    for re in records:
        r = re.split(" ")
        cal[r[1]].append([r[0], r[-1]])

    for (num, l) in cal.items():
        if len(l)%2 == 1:
            cal[num].append(['23:59', 'OUT'])

    cal = {i:cal[i] for i in sorted(cal)}
    m = []
    for v in cal.values():
        times = [i[0] for i in v]
        intime = times[::2]
        outtime = times[1::2]
        m.append(0)
        for i in range(len(outtime)):
            m[-1] += subTime (outtime[i], intime[i])
    
    answer = []
    for a in m:
        answer.append(fees[1])
        if a-fees[0] <= 0:
            continue
        else:
            if (a-fees[0])%fees[2] == 0:
                answer[-1] += ((a-fees[0])//fees[2] * fees[3])
            else:
                answer[-1] += (((a-fees[0])//fees[2] + 1) * fees[3])
    return answer
