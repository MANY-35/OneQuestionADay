# LV3 이중우선순위큐

### 1차 시도 (실패)
```py
from queue import PriorityQueue
def solution(operations):
    answer = []
    min_heap = PriorityQueue()
    max_heap = PriorityQueue()
    counter = [0, 0]
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            counter[0] += 1
            min_heap.put(num)
            max_heap.put(-num)
        elif op == "D":
            counter[1] += 1
            if num == 1:
                max_heap.get()
            elif num == -1:
                min_heap.get()
    if counter[0] <= counter[1]:
        return [0, 0]
    answer.append(-max_heap.get())
    answer.append(min_heap.get()) 
    return answer
```
최대값과 최소값을 계산하는 우선순위 큐를 두개 만들어서 접근했으나 시간초과가 발생했으며, 몇개의 케이스에서 실패했다. 생각해보니 큐에 더하는 연산과 빼는 연산의 단순한 수로 계산하는 것은 문제가있었다. 주어진 문제에선 큐가 비어있을때도 숫자를 삭제하는 연산이 가능하다는 사실을 간과했다.

*****

### 2차 시도 (실패)
```py
from queue import PriorityQueue
def solution(operations):
    min_heap = PriorityQueue()
    max_heap = PriorityQueue() 
    length = 0
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            min_heap.put(num)
            max_heap.put(-num)
            length += 1
        elif op == 'D':
            if length == 1:
                min_heap = PriorityQueue()
                max_heap = PriorityQueue()
                length = 0
            elif length > 1:
                if num == -1:
                    min_heap.get()
                elif num == 1:
                    max_heap.get()
                length -= 1
    return [-max_heap.get(), min_heap.get()] if length > 0 else [0, 0]
```

두개의 우선순위 큐를 동기화 해주기 위해 서로의 같은 길이를 설정하여 접근하였으나 3개의 케이스에서 실패했다.  
다시 생각하보니 단순히 길이를 조절해주는 것만으로는 한쪽에서 지운 값이 다른쪽 값에는 남아 있기에 삽입과 삭제에 영향을 미친다는 오류를 알 수 있었다.

******

### 3차 시도 (성공)
```py
from queue import PriorityQueue
def solution(operations):
    min_heap = PriorityQueue()
    max_heap = PriorityQueue() 
    entrys = []
    i = 0
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            min_heap.put((num, i))
            max_heap.put((-num, i))
            i += 1
            entrys.append(False)
        elif op == 'D':
            if num == 1:
                while not max_heap.empty():
                    n = max_heap.get()[1]
                    if not entrys[n]:
                        entrys[n] = True
                        break
            else:
                while not min_heap.empty():
                    n = min_heap.get()[1]
                    if not entrys[n]:
                        entrys[n] = True
                        break
    
    answer = [0, 0]
    while not max_heap.empty():
        n = max_heap.get()
        if not entrys[n[1]]:
            answer[0] = -n[0]
            break
    while not min_heap.empty():
        n = min_heap.get()
        if not entrys[n[1]]:
            answer[1] = n[0]
            break
    return answer
```

결국은 두개의 큐가 서로 가지고있는 값이 동기화 되어야 된다는 생각을 했고, 삽입된 숫자들에 키를 부여하여 몇번째 숫자가 삽입, 삭제 되었는지를 판단하는 배열을 선언하여 해당 배열의 위치를 키 값으로 판단하여 이미 다른큐에서 삭제된 값이라면 현재 큐를 계산할때 삭제하는 방식으로 접근하여 해결했다.

*****  

> ## **p.s.**  
> 코드를 좀더 깔끔하게 내부함수를 선언하여 정리해보았다.
> ```py
> from queue import PriorityQueue
> def solution(operations):
>     def func(que, entrys, flag=True):
>         while not que.empty():
>             n = que.get()
>             if not entrys[n[1]]:
>                 if flag:
>                     entrys[n[1]] = True
>                 return n[0]
>         return 0
>     
>     min_heap = PriorityQueue()
>     max_heap = PriorityQueue()
>     entrys = []
>     i = 0
>     for operation in operations:
>         op, num = operation.split()
>         num = int(num)
>         if op == 'I':
>             min_heap.put((num, i))
>             max_heap.put((-num, i))
>             i += 1
>             entrys.append(False)
>         elif op == 'D':
>             if num == 1:
>                 func(max_heap, entrys)
>             else:
>                 func(min_heap, entrys)
>     
>     return [-func(max_heap, entrys, False), func(min_heap, entrys, False)]
> ```
