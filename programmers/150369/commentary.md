# LV2 주차 요금 계산

### 1차시도 (실패)
```py
def solution(cap, n, deliveries, pickups):
    answer = 0
    tail = n-1
    while tail > 0:
        answer += ((tail+1) * 2)
        worker = cap
        temp = tail
        while worker > 0 and temp > 0:
            if deliveries[temp] <= worker:
                worker -= deliveries[temp]
                deliveries[temp] = 0
            else:
                deliveries[temp] -= worker
                worker = 0
            temp -= 1
        worker = cap
        while worker > 0 and tail > 0:        
            if pickups[tail] <= worker:
                worker -= pickups[tail]
                pickups[tail] = 0
            else:
                pickups[tail] -= worker
                worker = 0
            tail -= 1    
        if tail < temp:
            tail = temp
    return answer
```
tail 이라는 변수를 통해 트럭이 가야할 마지막 노드 까지를 계산하는 방식으로 풀어 보았으나 모든 케이스에서 실패했다.

*****

### 2차 시도(성공)
```py
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [[i+1, deliveries[i]] for i in range(len(deliveries)) if deliveries[i]]
    pickups = [[i+1, pickups[i]] for i in range(len(pickups)) if pickups[i]]

    while deliveries or pickups:
        i = 0
        if deliveries:
            i = deliveries[-1][0]
        j = 0
        if pickups:
            j = pickups[-1][0]
        answer += max(i, j) * 2    
        
        stack = 0
        while stack < cap and deliveries:
            last = deliveries.pop()
            stack += last[1]
        if stack > cap:
            deliveries.append([last[0], stack-cap])

        stack = 0
        while stack < cap and pickups:
            last = pickups.pop()
            stack += last[1]
        if stack > cap:
            pickups.append([last[0], stack-cap])
    return answer
```
비슷한 방식으로 풀되 스택을 이용하여 마지막 노드의 상자의 개수 만큼 빼고 짐칸이 남는다면 그 다음 노드에서 남은 짐의 개수 만큼 빼주는 식으로 풀었다.
