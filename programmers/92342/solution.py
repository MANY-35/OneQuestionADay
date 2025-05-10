from itertools import combinations
def solution(n, info):
    if info[0] == n:
        return [-1]
    db = []
    apeach = 0
    for i in range(len(info)):
        if info[i] > 0:
            apeach += 10-i
        db.append([i, info[i]+1])
    m = 0
    for i in range(1, 11):
        for j in combinations(db, i):
            sum = 0
            arr = list(j)
            shootCount = 0
            ap = apeach
            for k in j:
                shootCount+=k[1]
                sum += (10-k[0])
                if k[1] > 1:
                    ap -= 10-k[0]
            if n < shootCount:
                continue
            if n > shootCount:
                arr.append([10, n-shootCount])
            if m <= sum - ap:
                m = sum-ap
                n2 = ap
                n1 = sum
                temp = arr
    if n1 <= n2:
        return [-1]
    answer = [0 for _ in range(11)]
    for i in temp:
        answer[i[0]] = i[1]
    return answer