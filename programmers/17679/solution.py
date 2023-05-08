def solution(m, n, board):
    arr = [[c for c in l] for l in board]

    while True:
        b = [] 
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != 0 and arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] :
                    b.append([i,j])
        if b == []:
            break

        for i, j in b:
            arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = 0

        for i in range(n):
            for j in range(m):
                if arr[j][i] == 0:
                    for k in range(j):
                        t = arr[k][i]
                        arr[k][i] = arr[j][i]
                        arr[j][i] = t

    answer = 0
    for i in arr:
        answer += i.count(0)
    return answer