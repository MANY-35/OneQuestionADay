def solution(cards):
    visted = [False for _ in cards]
    groups = []
    for i in range(len(cards)):
        if visted[i]:
            continue
        j = cards[i]-1
        count = 0
        while not visted[j]:
            visted[j] = True
            count += 1
            j = cards[j]-1
        groups.append(count)
    answer = sorted(groups, reverse=True)[:2]
    return answer[0] * answer[1]

solution([8,6,3,7,2,5,1,4])