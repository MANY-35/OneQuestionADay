# LV2 양궁대회

### 1차 시도 (실패)
```py
def solution(n, info):
    if info[0] == n:
        return [-1]

    db = []
    for i in range(len(info)):
        t = [i, info[i]+1, 10-i]
        if info[i] > 0:
            t[-1] *= 2
        t[-1] /= info[i]+1
        db.append(t)

    db = sorted(db, key=lambda x:(-x[2], x[0]))
    t = 0
    answer = [0 for _ in range(11)]
    for d in db:
        if t + d[1] > n:
            continue
        answer[d[0]] = d[1]
        t += d[1]
    answer[-1] += n-t
    return answer
```
절반 정도의 케이스에서 성공했다. 화살 한 발의 기대값을 구하고 기대값이 가장 높은 점수부터 맞추는 방식으로 풀었다.  
기대값은 이미 어피치가 얻은 점수라면 *2를 하여 어피치의 점수를 뺏는 것을 고려했지만 알고리즘적으로 틀린 것 같다.

*****

# 2차 시도 (성공)
```py
from itertools import combinations
def solution(n, info):
    if info[0] == n:
        return [-1]
    db = []
    apeach = 0
    for i in range(len(info)):
        if info[i] > 0:
            apeach += 10-i
        db.append([i, info[i]+1])
    m = 0
    for i in range(1, 11):
        for j in combinations(db, i):
            sum = 0
            arr = list(j)
            shootCount = 0
            ap = apeach
            for k in j:
                shootCount+=k[1]
                sum += (10-k[0])
                if k[1] > 1:
                    ap -= 10-k[0]
            if n < shootCount:
                continue
            if n > shootCount:
                arr.append([10, n-shootCount])
            if m <= sum - ap:
                m = sum-ap
                n2 = ap
                n1 = sum
                temp = arr
    if n1 <= n2:
        return [-1]
    answer = [0 for _ in range(11)]
    for i in temp:
        answer[i[0]] = i[1]
    return answer
```
이전 풀이법에는 동점과 이기는 것이 불가능할 경우를 처리하는 과정이 잘못되었으며, 화살 한 발의 점수를 계산하는 것은 라이언이 가장 큰 점수를 얻는 방법은 맞으나 문제에서 요구하는 어피치와의 점수 차이가 가장 큰 것을 구하는 것에는 맞지 않은 풀이법이었다.  
따라서 과녁의 점수가 10점까지밖에 없다는 점을 이용하여 무차별 대입법을 이용하여 모든 경우를 구하는 것이 가장 적합하다는 것을 알아냈다.
