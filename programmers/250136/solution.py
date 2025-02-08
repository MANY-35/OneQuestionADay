import sys

sys.setrecursionlimit(1000000)

def solution(land):
    sumArr = [0 for _ in range(len(land[0]))]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if land[y][x] == 0:
                continue
            visit = set()
            sum = [0]
            bfs(land, x, y, visit, sum)
            for i in visit:
                sumArr[i-1] += sum[0]
    return max(sumArr)


def bfs(land, x, y, visit, sum):
    visit.add(x)
    land[y][x] = 0
    sum[0] += 1

    if y < len(land)-1:
        if land[y+1][x] == 1:
            bfs(land, x, y+1, visit, sum)
    if y > 0:
        if land[y-1][x] == 1:
            bfs(land, x, y-1, visit, sum)
    if x > 0:
        if land[y][x-1] == 1:
            bfs(land, x-1, y, visit, sum)
    if x < len(land[0])-1:
        if land[y][x+1] == 1:
            bfs(land, x+1, y, visit, sum)