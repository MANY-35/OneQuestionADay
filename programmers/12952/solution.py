def dfs(indexes, n, row, count):
    if row == n:
        count[0] += 1
        return
    arr = []
    for i in range(n):
        flag = True
        for r, c in indexes:
            if abs(row-r) == abs(c-i) or i == c:
                flag = False
                break
        if flag:
            arr.append(i)
    for i in arr:
        indexes.append((row, i))
        dfs(indexes, n, row+1, count)
        indexes.pop()
def solution(n):
    poss = []
    answer = [0]
    dfs(poss, n, 0, answer)
    return answer.pop()

solution(4)