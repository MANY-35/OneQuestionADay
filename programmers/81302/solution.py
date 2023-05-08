def solution(places):
    def func(pi):
        for i in range(len(pi)-1):
            for j in range(i+1, len(pi)):
                if abs(pi[i][0] - pi[j][0]) + abs(pi[i][1] - pi[j][1]) <= 2:
                    t = [[place[x][y] for y in range(min(pi[i][1], pi[j][1]), max(pi[i][1], pi[j][1])+1)] for x in range(min(pi[i][0], pi[j][0]), max(pi[i][0], pi[j][0])+1)]
                    count = 0
                    for ti in t:
                        count += ti.count('X')
                    if count < len(t[0]) and count < len(t):
                        return 0
        return 1
    
    answer = []
    for place in places:
        pi = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    pi.append([i,j])
        answer.append(func(pi))
    return answer