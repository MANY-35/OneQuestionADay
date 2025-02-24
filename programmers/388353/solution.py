def solution(storage, requests):
    answer = 0
    arr = [[0 for _ in range(len(storage[0])+2)] for _ in range(len(storage)+2)] 
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            arr[1+i][1+j] = storage[i][j]
    
    for request in requests:
        vist = []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == request[0]:
                    if len(request) > 1:
                        arr[i][j] = 1
                    else:
                        if finder(arr, i, j):
                            vist.append((i,j))
        for y,x in vist:
            arr[y][x] = 0                
                
    for a in arr:
        for c in a:
            if c != 0 and c != 1:
                answer += 1
    return answer


def finder(arr, r, c):
    vist = set()
    que = [(r,c)]
    while que:
        y, x = que.pop()
        if x == 0 or x == len(arr[0]) or y == 0 or y == len(arr):
            continue
        vist.add((y,x))
        for i, j in [[1, 0], [0, 1], [-1,0], [0, -1]]:
            if arr[y+i][x+j] == 0:
                return True
            elif arr[y+i][x+j] == 1 and ((y+i),(x+j)) not in vist:
                que.append(((y+i),(x+j)))
    return False

solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])