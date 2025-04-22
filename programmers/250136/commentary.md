# LV2 [PCCP 기출문제] 2번 / 석유 시추

### 1차 시도(실패)
```py
def solution(land):
    sumArr = [0 for _ in range(len(land[0]))]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if land[y][x] == 0:
                continue
            visit = set()
            sum = [0]
            dfs(land, x, y, visit, sum)
            for i in visit:
                sumArr[i-1] += sum[0]
    return max(sumArr)

def dfs(land, x, y, visit, sum):
    if land[y][x] == 0:
        return
    
    visit.add(x)
    land[y][x] = 0
    sum[0] += 1

    if y < len(land)-1:
        dfs(land, x, y+1, visit, sum)
    if y > 0:
        dfs(land, x, y-1, visit, sum)
    if x > 0:
        dfs(land, x-1, y, visit, sum)
    if x < len(land[0])-1:
        dfs(land, x+1, y, visit, sum)
```
> 정확성 테스트는 모두 통과하였으나 효율성 부분에서 에러가 발생했다. 찾아보니 재귀함수를 너무 많이 들어가는게 문제가 생기는 것 같다.

*****

### 2차시도 (성공)
```py
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
```
> 단순하게 재귀의 최대값을 제한하는 방식으로 해결이 가능했지만 문제에서 요구하는 방법은 아닌 것 같다.
