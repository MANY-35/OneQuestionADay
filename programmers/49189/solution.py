def solution(n, edge):
    vist = [True for _ in range(n)]
    arr = [[] for _ in range(n)]
    for a, b in edge:
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)
    que = [[0]]
    vist[0] = False
    while que[-1]:
        t = []
        for i in que[-1]:
            for j in range(len(arr[i])):
                if vist[arr[i][j]]:
                    t.append(arr[i][j])
                    vist[arr[i][j]] = False
        que.append(t)
    return len(que[-2])