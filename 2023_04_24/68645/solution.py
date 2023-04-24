def solution(N):
    arr = [[0]*j for j in range(1, N+1)]
    x = 0
    y = -1
    xi = 0
    yi = num = 1

    for i in range(N):
        for j in range(N-i):
            y += yi
            x += xi
            arr[y][x] = num
            num += 1
        yi -= 1
        if yi < -1:
            yi = 1
        xi += 1
        if xi > 1:
            xi = -1
        
    answer = []     
    for i in arr:
        answer += i
                    
    return answer

print(solution(7))