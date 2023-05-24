def solution(m, n, puddles):
    arr = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for p in puddles:
        arr[p[1]][p[0]] = -1
    arr[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j] < 0:
                continue        
            t = arr[i][j]
            if arr[i-1][j] > 0:
                t += arr[i-1][j]
            if arr[i][j-1] > 0:
                t += arr[i][j-1]
            arr[i][j] = t
    return arr[-1][-1] % 1000000007