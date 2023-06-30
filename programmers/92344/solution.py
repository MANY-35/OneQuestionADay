board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]


def solution(board, skill):
    arr = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    Sarr = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for t, r1, c1, r2, c2, d in skill:
        t = t*2 - 3
        arr[r1][c1] += t*d
        arr[r2+1][c1] += t*-d
        arr[r1][c2+1] += t*-d

    for k in arr:
        print(k)
    print()

    for i in range(1, len(arr)):
        arr[i][0] += arr[i-1][0]
    for j in range(1, len(arr[0])):
        arr[0][j] += arr[0][j-1]
    
    for k in arr:
        print(k)
    print()

    i, j = 1, 1 
    while i<len(arr) and j<len(arr):
        
        
        for ii in range(i, len(arr)):
            arr[ii][j] += arr[ii-1][j]
            Sarr[ii][j] = arr[ii-1][j-1] + Sarr[ii-1][j] + Sarr[ii][j-1] - Sarr[ii-1][j-1]
        for jj in range(j, len(arr[i])):
            arr[i][jj] += arr[i][jj-1]
            Sarr[i][jj] = arr[i-1][jj-1] + Sarr[i][jj-1] + Sarr[i-1][jj] - Sarr[i-1][jj-1]

        arr[i][j] -= arr[i-1][j-1]

        for k in arr:
            print(k)
        print()

        for k in Sarr:
            print(k)
        print()
        
        
        
        i +=1
        j +=1
        
    return 0

solution(board, skill)