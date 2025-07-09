# LV2 과제 진행하기

### 1차시도 (실패)
```py
def solution(plans):
    answer = []
    for i in range(len(plans)):
        t = plans[i][1].split(':')
        plans[i][1] = int(t[0]) * 60 + int(t[1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    
    que = [plans[0]]
    time = plans[0][1]
    for i in range(1, len(plans)):
        if not que:
            que.append(plans[i])
            time = plans[i][1]
            continue
        if time + que[-1][2] > plans[i][1]:
            que[-1][2] -= plans[i][1] - time
            time = plans[i][1]
        else:
            while que and time + que[-1][2] <= plans[i][1]:
                answer.append(que[-1][0])
                que.pop()
        que.append(plans[i])
    while que:
        answer.append(que[-1][0])
        que.pop()
    return answer
```

대기 큐를 만들고 앞으로 수행해야하는 과제와 대기중인 과제들의 시간을 비교하여 푸는 방식으로 접근해보았다.  
하지만 절반정도의 케이스에서 실패 했다.

*****

### 2차시도 (실패)
```py
def solution(plans):
    answer = []
    for i in range(len(plans)):
        t = plans[i][1].split(':')
        plans[i][1] = int(t[0]) * 60 + int(t[1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    
    que = [plans[0]]
    time = plans[0][1]
    for i in range(1, len(plans)):
        if not que:
            que.append(plans[i])
            time = plans[i][1]
            continue
        if time + que[-1][2] > plans[i][1]:
            que[-1][2] -= plans[i][1] - time
        else:
            while que and time + que[-1][2] <= plans[i][1]:
                time += que[-1][2]
                answer.append(que[-1][0])
                que.pop()
        que.append(plans[i])
        time = plans[i][1]
    while que:
        answer.append(que[-1][0])
        que.pop()
    return answer
```
이전 코드에서 대기 큐에 있던 과제들을 먼저 수행하는 경우에 시간의 진행을 계산하지 않았다는 것을 깨닫고 이를 수정했다.  
4개의 케이스에서 실패했다. 다른 예외를 찾아봐야 할 것 같다.

*****

### 3차시도 (성공)
```py
def solution(plans):
    answer = []
    for i in range(len(plans)):
        t = plans[i][1].split(':')
        plans[i][1] = int(t[0]) * 60 + int(t[1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    que = [plans[0]]
    time = plans[0][1]
    for i in range(1, len(plans)):
        while que and time + que[-1][2] <= plans[i][1]:
            time += que[-1][2]
            answer.append(que[-1][0])
            que.pop()
        if que:
            que[-1][2] -= plans[i][1] - time
        que.append(plans[i])
        time = plans[i][1]
    while que:
        answer.append(que[-1][0])
        que.pop()
    return answer
```
이전에 수정했던 시간의 진행을 항상 마지막 시간으로 저장하는 바람에 마지막으로 진행하던 과제에 대해 시간을 차감하지 않아 발생한 문제였다.  
이를 수정 하면서 이전에 있던 조건문들이 필요없어지면서 코드가 간단해졌다.

*****
