# LV3 기지국 설치

### 1차 시도 (성공)
```py
def solution(n, stations, w):
    temp = []
    t = 0
    for s in stations:
        temp.append(s-w-t-1)
        t = s+w
    temp.append(n-t)
    temp = [i for i in temp if i>0]

    answer = 0
    k = w*2+1
    for t in temp:
        answer += t // k
        if t%k > 0:
            answer += 1
    return answer
```
이미 설치된 기지국을 기준으로 전파가 닿지 않는 연속된 아파트들의 개수를 구한 뒤, 해당 구간에 몇 개의 기지국이 필요한지 세는 방식으로 풀었다.