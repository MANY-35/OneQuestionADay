# LV2 두 큐 합 같게하기

### 1차시도 (실패)
```py
def solution(queue1, queue2):
    answer = 0
    check = queue1.copy()
    q1 = sum(queue1)
    q2 = sum(queue2)
    if (q1+q2) % 2 != 0:
        return -1
    
    while q1 != q2:
        answer += 1
        if q1 > q2:
            queue2.append(queue1.pop(0))
        else:
            queue1.append(queue2.pop(0))
        q1 = sum(queue1)
        q2 = sum(queue2)

        print(check, queue1)
        if check == queue1:
            return -1
    return answer
```
> 대부분 성공했으나 몇몇 케이스에 대해서 시간이 초과되었다. 큐가 충분히 크면 반복에 문제가 발생하는듯 하다.

*****

### 2차시도 (실패)
```py
from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    que1 = deque(queue1)
    que2 = deque(queue2)
    check = q1 = sum(que1)
    q2 = sum(que2)
    
    if (q1+q2) % 2 != 0:
        return -1
    
    while q1 != q2:
        answer += 1
        if q1 > q2:
            que2.append(que1.popleft())
        else:
            que1.append(que2.popleft())
        q1 = sum(que1)
        q2 = sum(que2)

        if check == q1:
            return -1
    return answer
```
> 리스트에서 데큐로 자료형을 변경하여 추가 삭제할때 시간을 줄여보았다. 그러나 여전히 시간이 초과되는 케이스가 있는가 하면 실패하는 케이스가 생겼다.

*****

### 3차시도 (실패)
```py
from collections import deque
def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)
    check = deque(queue1)
    q1 = sum(que1)
    q2 = sum(que2)
    if (q1+q2) % 2 != 0:
        return -1
    
    while q1 != q2:
        answer += 1
        if q1 > q2:
            t = que1.popleft()
            que2.append(t)            
            q1 -= t
            q2 += t
        else:  
            t = que2.popleft()
            que1.append(t)         
            q2 -= t
            q1 += t
        
        if check == que1:
            return -1
    return answer
```
> 이전 코드에서 sum함수로 전체의 합을 구하는 것이아니라 방금 뺀 값을 통해 합을 계산하여 시간을 줄였다.
> 하지만 단 하나의 데이터 케이스에서 시간이 초과했다.

*****

### 4차시도 (성공)
```py
def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)
    q1 = sum(que1)
    q2 = sum(que2)
    qs = q1 + q2
    if qs % 2 != 0:
        return -1
    check = 0
    while q1 != q2:
        answer += 1
        if q1 > q2:
            t = que1.popleft()
            que2.append(t)            
            q1 -= t
            q2 += t
        else:  
            t = que2.popleft()
            que1.append(t)         
            q2 -= t
            q1 += t
        check += t
        if check >= qs*2:
            return -1
    return answer
```
> 각 큐에서 값들이 움직이면서 원래의 모양과 같은 상황이 오지 않는 경우를 고려하지 않았다. 그래서 값이 움직일때마다 움직인 값을 저장하여 그 값이 모든 배열의 합의 두배 보다 많다는 것은 모든 원소들이 최소 한번씩은 움직였고, 그 때 까지 큐의 값이 서로 같지 않다는 것은 같은 값으로 만드는 것이 불가능하다는 것을 나타낸다고 생각했다.
