def solution(k, ranges):
    answer = []

    sumArr = [0]
    be = k
    while be != 1:
        if be % 2 == 0:
            n = be // 2
        else:
            n = be * 3 + 1
        if n < be:
            area = n + (be-n)/2
        else:
            area = be + (n-be)/2
        sumArr.append(sumArr[-1] + area)
        be = n
    for a, b in ranges:
        b = len(sumArr)-1 + b
        if a > b:
            answer.append(-1.0)
        else:
            answer.append(sumArr[b] - sumArr[a])
    print(answer)
    return answer

solution(5, [[0,0],[0,-1],[2,-3],[3,-3], [2, 0]])