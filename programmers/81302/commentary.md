# LV2 두 큐 합 같게하기

### 1차시도 (실패)
```py
def solution(places):
    N = 5
    def check (arr):
        if arr[1][0] == "P" or arr[0][1] == 'P' or arr[2][1] == 'P' or arr[1][2] == "P":
            return True
        elif arr[0][0] == 'P':
            if arr[1][0] != 'X' or arr[0][1] != 'X':
                return True
        elif arr[0][2] == 'P':
            if arr[1][2] != 'X' or arr[0][1] != 'X':
                return True
        elif arr[2][0] == 'P':
            if arr[1][0] != 'X' or arr[2][1] != 'X':
                return True
        elif arr[2][2] == 'P':
            if arr[1][2] != 'X' or arr[2][1] != 'X':
                return True   
        return False

    def func(arr, N):
        for i in range(1,N-1):
            for j in range(1, N-1):
                if arr[i][j] == 'P':
                    t = [[arr[y][x] for x in range(j-1, j+2)] for y in range(i-1, i+2)]
                    if check(t):
                        return 0
        return 1

    answer = []
    arr = [['X' for _ in range(N+2)] for _ in range(N+2)]
    for place in places:
        for i in range(N):
            for j in range(N):
                arr[1+i][1+j] = place[i][j]
        answer.append(func(arr, N+2))
    return answer
```
3가지의 케이스에서 실패 했다. 주어진 조건에서 놓친 부분이 있는 것 같다.

*****

### 2차시도 (실패)
```py
def solution(places):
    def func(pi):
        for i in range(len(pi)-1):
            for j in range(i+1, len(pi)):
                if abs(pi[i][0] - pi[j][0]) + abs(pi[i][1] - pi[j][1]) <= 2:
                    xi = range(min(pi[i][0], pi[j][0]), max(pi[i][0], pi[j][0])+1)
                    yi = range(min(pi[i][1], pi[j][1]), max(pi[i][1], pi[j][1])+1)
                    t = [[place[x][y] for y in yi] for x in xi]
                    for ti in t:
                        if 'O' in ti:
                            return 0
        return 1
    answer = []
    for place in places:
        pi = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    pi.append([i,j])
        answer.append(func(pi))
    return answer
```
이전 코드에서 주어진 조건인 맨해튼 거리의 게산을 잘못 판단하여 틀렸던 것을 깨닫고 다른 방식으로 접근했는데 절반의 데이터 케이스에서 실패했다.  
func 함수에서 return이 포함된 if 문을 수정해야 할 것 같다.

*****

### 3차시도 (성공)
```py
def solution(places):
    def func(pi):
        for i in range(len(pi)-1):
            for j in range(i+1, len(pi)):
                if abs(pi[i][0] - pi[j][0]) + abs(pi[i][1] - pi[j][1]) <= 2:
                    t = [[place[x][y] for y in range(min(pi[i][1], pi[j][1]), max(pi[i][1], pi[j][1])+1)] for x in range(min(pi[i][0], pi[j][0]), max(pi[i][0], pi[j][0])+1)]
                    count = 0
                    for ti in t:
                        count += ti.count('X')
                    if count < len(t[0]) and count < len(t):
                        return 0
        return 1

    answer = []
    for place in places:
        pi = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    pi.append([i,j])
        answer.append(func(pi))
    return answer
```
이전 조건에서는 단순히 O가 없어야 된다고 생각했지만 O가 존재해도 X로인해 서로 분리된 경우의 수를 생각하지 못했었다.  
곰곰히 생각하다가 위와 같은 조건을 생각해 냈다.