# LV2 [PCCP 기출문제] 3번 / 충돌 위험 찾기

### 1차 시도(성공)
```py
def move(s, e):
    if(s[0]>e[0]):
        return [s[0]-1, s[1]]
    elif(s[0] < e[0]):
        return [s[0]+1, s[1]]
    else:
        if(s[1]>e[1]):
            return [s[0], s[1]-1]
        elif(s[1]<e[1]):
            return [s[0], s[1]+1]
        else:
            return e

def solution(points, routes):
    answer = 0

    botCount = len(routes)
    endpoint = len(routes[0])
    
    dests = [1 for _ in routes]
    bots = [points[i[0]-1] for i in routes]
    
    checkSet = {}
    for bot in bots:
        k = str(bot)
        if k not in checkSet.keys():
            checkSet[k] = 1
        else:
            checkSet[k] += 1
    while True:
        for v in checkSet.values():
            if v > 1:
                answer += 1
                    
        if sum(dests) == botCount*endpoint:
            break
        
        checkSet = {}
        for i in range(botCount):
            if dests[i] < endpoint:
                bots[i] = move(bots[i], points[routes[i][dests[i]]-1])
                if bots[i] == points[routes[i][dests[i]]-1]:
                    dests[i] += 1
                
                k = str(bots[i])
                if k not in checkSet.keys():
                    checkSet[k] = 1
                else:
                    checkSet[k] += 1
    return answer
```
