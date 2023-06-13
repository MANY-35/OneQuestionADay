from collections import defaultdict
import copy
def func(dc:dict, answer:list, now, l, k):
    if len(answer) > l:
        k.append(answer)
        return
    elif dc[now] == []:
        return

    for i in range(len(dc[now])):
        print(dict(dc))
        t = answer.copy()
        tdc = copy.deepcopy(dc)
        n = tdc[now].pop(i)
        t.append(n)
        func(tdc, t, n, l, k)
    
def solution(tickets):
    dc = defaultdict(list)
    for s, e in tickets:
        dc[s].append(e)
    start = 'ICN'
    answer = [start]
    k = []
    func(dc, answer, start, len(tickets), k)
    return sorted(k)[0]
