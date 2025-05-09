# LV2 행렬 테두리 회전하기

### 1차시도 (성공)
```py
from collections import deque
def solution(rows, columns, queries):
    arr = [[(j*columns) + i for i in range(1, columns+1)] for j in range(rows)]
    answer = []
    for query in queries:
        q = [i-1 for i in query]
        dque = deque([])

        for x in range(q[1], q[3]):
            dque.append(arr[q[0]][x])
        for y in range(q[0], q[2]):
            dque.append(arr[y][q[3]])
        for x in range(q[3], q[1], -1):
            dque.append(arr[q[2]][x])
        for y in range(q[2], q[0], -1):
            dque.append(arr[y][q[1]])

        answer.append(min(dque))
        dque.appendleft(dque.pop())

        for x in range(q[1], q[3]):
            arr[q[0]][x] = dque.popleft()
        for y in range(q[0], q[2]):
            arr[y][q[3]] = dque.popleft()
        for x in range(q[3], q[1], -1):
            arr[q[2]][x] = dque.popleft()
        for y in range(q[2], q[0], -1):
            arr[y][q[1]] = dque.popleft()
    return answer
```
테두리를 탐색할 수 있는 알고리즘을 계속 고민해봤는데 실마리가 보이지 않아 네 번의 반복문을 통해 직선으로 4방향을 탐색했다.  
다른 사람들의 풀이를 봐도 명확하게 좋다고 판단할만한 알고리즘을 발견하지 못했다. 좀더 연구를 해봐야 할 것 같다.