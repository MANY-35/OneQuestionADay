# LV2 혼자 놀기의 달인

### 1차시도 (성공)
```py
def solution(cards):
    visited = [False for _ in cards]
    groups = []
    for i in range(len(cards)):
        if visited[i]:
            continue
        j = cards[i]-1
        count = 0
        while not visited[j]:
            visited[j] = True
            count += 1
            j = cards[j]-1
        groups.append(count)
    if len(groups) < 2:
        return 0
    answer = sorted(groups, reverse=True)[:2]
    return answer[0] * answer[1]

```

주어진 문제는 가능한 가장 큰 두 그룹의 곱을 구하는 것이기 때문에 간단히 모든 그룹을 구하는 방식으로 접근했다.  
visited 배열을 만들어 이미 방문한 그룹인지 판단하도록 코드를 작성했다.

*****
