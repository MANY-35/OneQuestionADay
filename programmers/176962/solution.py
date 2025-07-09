def solution(plans):
    answer = []
    for i in range(len(plans)):
        t = plans[i][1].split(':')
        plans[i][1] = int(t[0]) * 60 + int(t[1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    que = [plans[0]]
    time = plans[0][1]
    for i in range(1, len(plans)):
        while que and time + que[-1][2] <= plans[i][1]:
            time += que[-1][2]
            answer.append(que[-1][0])
            que.pop()
        if que:
            que[-1][2] -= plans[i][1] - time
        que.append(plans[i])
        time = plans[i][1]
    while que:
        answer.append(que[-1][0])
        que.pop()
    return answer
solution([[ "A", "00:00", "60" ] , [ "B", "00:10", "60" ] , [ "C", "00:20", "60" ] , [ "D", "02:20", "60" ] , [ "E", "03:20", "10" ] , [ "F", "03:40", "20" ], ["G", "04:40", "60" ]])