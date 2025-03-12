from collections import deque

def solution(players, m, k):
    que = deque()
    n = 0
    count = 0
    for time in range(len(players)):
        if players[time] >= (n+1)*m:
            print(time, players[time], n)
            temp = n
            n = players[time] // m
            temp = n - temp
            count += temp
            que.append((temp, time+k-1))
        if que:
            if que[0][1] == time:
                temp = que.popleft()
                n -= temp[0]
    
    return count

print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0],5,1))