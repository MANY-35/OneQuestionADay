# LV3 표 편집

### 1차시도 (실패)
```py
def solution(n, k, cmd):
    arr = [True for _ in range(n)]
    last = []
    for s in cmd:
        c = s.split()
        if c[0] == 'D':
            i = int(c[1])
            while i > 0:
                i-=1
                k+=1
                if not arr[k]:
                    i+=1

        elif c[0] == 'U':
            i = int(c[1])
            while i > 0:
                i-=1
                k-=1
                if not arr[k]:
                    i+=1

        elif c[0] == 'C':
            arr[k] = False
            last.append(k)
            if k == n-1:
                k-=1
            else:
                k+=1
        elif c[0] == 'Z':
            arr[last.pop()] = True

    answer = ""       
    for i in arr:
        if i:
            answer+='O'
        else:
            answer+='X'
    return answer
```
단순히 주어진 조건대로 수행하도록 작성했으나 당연하게도 시간초과가 발생했으며 일부 정확성에서 조차 절반정도 틀렸다.  
그 중 런타임 에러가 있는 것으로 보아 배열 인덱스에 관한 오류인 것으로 보인다.

*****

### 2차시도 (실패)
```py
def solution(n, k, cmd):
    arr = [True for _ in range(n)]
    last = []
    for command in cmd:
        c = command.split()

        if c[0] == 'D':
            move = int(c[1])
            for i in sorted(last):
                if i > k and i <= k+move:
                    move+=1
            k += move

        elif c[0] == 'U':
            move = int(c[1])
            for i in sorted(last):
                if i < k and i >= k-move:
                    move+=1
            k -= move

        elif c[0] == 'C':
            arr[k] = False
            last.append(k)
            if k == n-1:
                k-=1
            else:
                k+=1
        elif c[0] == 'Z':
            arr[last.pop()] = True

    answer = ""       
    for i in arr:
        if i:
            answer+='O'
        else:
            answer+='X'
    return answer
```
수행 횟수를 줄이고자 지워진 데이터들이 있는 배열을 활용하려고 하였으나, 더 많은 케이스에서 시관초과가 발생했으며 더 많은 케이스에서 실패했고, 더 많은 에러가 발생했다.

*****

### 3차시도 (실패)
```py
def solution(n, k, cmd):
    karr = [[1,1] for _ in range(n+2)]
    karr[0] = [0,1]
    karr[-1] = [1,0]
    arr = [True for _ in range(n+2)]
    last = []
    k+=1
    for command in cmd:
        c = command.split()

        if c[0] == 'D':
            for i in range(int(c[1])):
                k += karr[k][1]

        elif c[0] == 'U':
            for i in range(int(c[1])):
                k -= karr[k][0]

        elif c[0] == 'C':
            arr[k] = False
            last.append(k)

            karr[k-karr[k][0]][1] += karr[k][1]
            karr[k+karr[k][1]][0] += karr[k][0]

            if k + karr[k][1] < n:
                k += karr[k][1]
            else:
                k -= karr[k][0]   

        elif c[0] == 'Z':
            d = last.pop()

            arr[d] = True
            karr[d-karr[d][0]][1] = karr[d][0]
            karr[d+karr[d][1]][0] = karr[d][1]

    answer = ""       
    for i in arr[1:-1]:
        if i:
            answer+='O'
        else:
            answer+='X'
    return answer
```
바로 다음 갈 수 있는 노드를 저장한 배열을 만들어 반복 없이 바로 노드를 이동하도록 코드를 작성해보았다.  
시간초과 문제는 해결했으나 몇개의 케이스에서 실패했다.  
예외 처리의 문제로 보인다.

*****

### 4차시도 (성공)
```py
def solution(n, k, cmd):
    karr = [[1,1] for _ in range(n+2)]
    karr[0] = [0,1]
    karr[-1] = [1,0]
    arr = [True for _ in range(n+2)]
    last = []
    k+=1
    for command in cmd:
        c = command.split()

        if c[0] == 'D':
            for i in range(int(c[1])):
                k += karr[k][1]

        elif c[0] == 'U':
            for i in range(int(c[1])):
                k -= karr[k][0]

        elif c[0] == 'C':
            arr[k] = False
            last.append(k)

            karr[k-karr[k][0]][1] += karr[k][1]
            karr[k+karr[k][1]][0] += karr[k][0]

            if k + karr[k][1] <= n:
                k += karr[k][1]
            else:
                k -= karr[k][0]   

        elif c[0] == 'Z':
            d = last.pop()

            arr[d] = True
            karr[d-karr[d][0]][1] = karr[d][0]
            karr[d+karr[d][1]][0] = karr[d][1]

    answer = ""       
    for i in arr[1:-1]:
        if i:
            answer+='O'
        else:
            answer+='X'
    return answer
```
이전 코드에서 마지막노드의 위치를 설정하는 조건문 *if k + karr[k][1] < n* 을 잘못 설정하여 발생한 문제였음. s