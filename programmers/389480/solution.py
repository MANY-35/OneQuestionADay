def solution(info, n, m):
    answer = 0
    info = sorted(info, key=lambda x: (x[1]-x[0]))
    sum = 0
    for data in info:
        if sum + data[1] < m:
            sum += data[1]
        else:
            answer += data[0]
            
    if answer >= n:
        return -1
    return answer
    
    

print(solution(	[[1, 2], [2, 2], [2, 1]], 4, 4))