def solution(picks, minerals):
    answer = 0

    maxCount = int(sum(picks)) * 5
    if maxCount < len(minerals):
        minerals = minerals[:maxCount] 
    if not minerals:
        return answer
    
    arr = []
    s = 0
    for i in range(len(minerals)):
        if not i % 5 and i != 0:
            arr.append(s)
            s = 0
        if minerals[i] == 'diamond':
            s += 100
        elif minerals[i] == 'iron':
            s += 10
        else:
            s += 1
    arr.append(s)
    arr = sorted(arr)
    board = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    for i in range(len(picks)):
        for _ in range(picks[i]):
            if not arr:
                return answer
            now = arr.pop()

            for k in range(2, -1, -1):
                answer += board[i][k] * (now % 10)
                now //= 10
    return answer

print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))