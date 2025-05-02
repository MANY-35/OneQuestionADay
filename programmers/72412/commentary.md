# Lv2 순위 검색

### 1차 시도 (실패)
```py
def func(board, code, x):
    arr = []
    for i in board.keys():
        for j in range(4):
            if code[j] == '0':
                continue
            elif code[j] != i[j]:
                j -= 1
                break
        if j == 3:
            arr.append(i)
    s=0
    for i in arr:
        for j in board[i]:
            if int(j) >= int(x):
                s += 1
    return s
def solution(info, query):
    code = [{"-":'0',"cpp":"1", "java":'2', "python":'3'},
        {"-":'0', "backend":'1', "frontend":'2'},
        {"-":'0', "junior":'1', "senior":'2'}, 
        {"-":'0', "chicken":'1', "pizza":'2'}]
    
    board = {}
    for i in info:
        arr = i.split(" ")
        c = ""
        for j in range(len(arr)-1):
            c += code[j][arr[j]]
        if c in board.keys():
            board[c].append(arr[4])
        else:
            board[c] = [arr[4]]

    answer = []
    for q in query:
        arr = q.replace(" and ", " ").split(" ")
        c = ""
        for j in range(len(arr)-1):
            c += code[j][arr[j]]
        answer.append(func(board, c, arr[-1]))
    return answer
```
모든 케이스에서 통과하였으나 효율성 테스트에서 시간 초과가 발생함 어떤 부분에서 시간을 줄일 수 있는지 찾아봐야한다.

*****

### 2차 시도 (실패)
```py
def solution(info:list[list], query:list[list]):
    p = []
    for i in info:
        p.append(i.split(" "))
    
    answer = []
    for q in query:
        c = 0
        q = q.replace(" and ", " ").split(" ")
        for i in p:
            for j in range(4):
                if q[j] == '-':
                    continue
                elif q[j] != i[j]:
                    j-=1
                    break
            if j == 3:
                if int(q[-1]) <= int(i[-1]):
                    c += 1        
        answer.append(c)
    return answer
```
1차 시도에서 따로 dict에 저장하지 않고 바로 탐색해서 출력하도록 코드를 수정했지만 여전히 시간 초과가 발생함

*****

### 3차시도 (성공)
```py
import bisect
def solution(info, query):
    board = {}
    for j0 in ['cpp', 'java', 'python', '-']:
        for j1 in ['backend', 'frontend', '-']:
            for j2 in ['junior', 'senior', '-']:
                for j3 in ['chicken', 'pizza', '-']:
                    board[j0+j1+j2+j3] = []
    for i in info:
        arr = i.split(" ")
        for j0 in [arr[0], '-']:
            for j1 in [arr[1], '-']:
                for j2 in [arr[2], '-']:
                    for j3 in [arr[3], '-']:
                        board[j0+j1+j2+j3].append(int(arr[-1]))
    for i in board.values():
        i.sort()
    answer = []
    for q in query:
        arr = q.replace(" and ", "").split()
        t = board[arr[0]]
        answer.append(len(t)-bisect.bisect_left(t, int(arr[-1])))
    return answer
```
> ~~도저히 방법을 모르겠어서 검색을 통해 해결했다.~~  

우선 시간복잡도를 줄이기 위해 공간복잡도를 증가시키는 방향으로 모든 경우의 수에 해당하는 딕셔너리를 만들고 그 딕셔너리에 값을 저장한후 출력하는 형식으로 코드를 작성하고, 특정 값을 찾는 것 또한 시간을 줄이기 위해 이분탐색을 이용하여 값을 찾도록 코드를 작성함.