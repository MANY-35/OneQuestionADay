# LV3 디스크 컨트롤러

### 1차시도 (실패)
```py
import heapq
def solution(jobs):
    que = []
    for job in jobs:
        heapq.heappush(que, (job[1]-job[0], job))

    answer = 0
    arr = [heapq.heappop(que)]
    time = arr[0][1][0]
    while time < 2001:
        if que == [] and arr == []:
            return answer/len(jobs)
        while que:
            if que[0][1][0] <= time:
                m = heapq.heappop(que)
                heapq.heappush(arr, m)
            else:
                break

        n = heapq.heappop(arr)
        answer += n[0] + time
        time += n[1][1]
    return answer/len(jobs)
```
하나의 케이스에서 정답이 나오고 나머지는 실패했다.  
런타임 에러가 발생한것으로 보아 심각하게 잘못된 부분이 있는듯하다.

*****

### 2차시도 (실패)
```py
import heapq
def solution(jobs):
    t = sorted(jobs, key=lambda x:x[0], reverse=True)
    k = t.pop()
    arr = [(k[1], k[0])]
    answer = 0
    time = arr[0][1]
    while time <= 2001:
        if t == [] and arr == []:
            return answer//len(jobs)
        while t:
            if t[-1][0] <= time:
                m = t.pop()
                heapq.heappush(arr, (m[-1], m[0]))
            else:
                break
        if arr:
            n = heapq.heappop(arr)
            answer += (time-n[1])+n[0]
            time += n[0]
        else:
            time += 1
    return answer//len(jobs)
```
딱 절반의 케이스에서 실패했다.  
이전 코드에서 입력값을 잘못 해석하여 문제가 발생했었고 이를 수정했다.

*****

### 3차시도 (성공)
```py
import heapq
def solution(jobs):
    t = sorted(jobs, key=lambda x:x[0], reverse=True)
    k = t.pop()
    arr = [(k[1], k[0])]
    answer = 0
    time = arr[0][1]
    while True:
        if t == [] and arr == []:
            return answer//len(jobs)
        while t:
            if t[-1][0] <= time:
                m = t.pop()
                heapq.heappush(arr, (m[-1], m[0]))
            else:
                break
        if arr:
            n = heapq.heappop(arr)
            answer += (time-n[1])+n[0]
            time += n[0]
        else:
            time += 1
    return answer//len(jobs)
```
이전코드에서 time의 제한을 2000으로 생각한 것이 잘못된 점이였다.  
각 작업에 요청되는 시간이 최대 1000이고 소요시간이 최대 1000인점에서 마지막시간에 최대가 요청되는 경우가 최악이라 판단하여 2000이 최대라고 생각한 것이 틀렸다.  
마지막에 요청되는 작업의 수가 500개 일 수 있기 때문이다.