# LV2 미로 탈출 명령어

### 1차시도 (성공)
```py
def solution(picks, minerals):
    answer = 0

    maxCount = int(sum(picks)) * 5
    if maxCount < len(minerals):
        minerals = minerals[:maxCount] 
    if not minerals:
        return answer
    
    arr = []
    s = 0
    for i in range(len(minerals)):
        if not i % 5 and i != 0:
            arr.append(s)
            s = 0
        if minerals[i] == 'diamond':
            s += 100
        elif minerals[i] == 'iron':
            s += 10
        else:
            s += 1
    arr.append(s)
    arr = sorted(arr)
    board = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    for i in range(len(picks)):
        for _ in range(picks[i]):
            if not arr:
                return answer
            now = arr.pop()

            for k in range(2, -1, -1):
                answer += board[i][k] * (now % 10)
                now //= 10
    return answer
```

주어진 피로도가 5배씩 늘어나는 점에서 세자리 자연수에 각각 다이아몬드, 철, 돌을 배치하여 가중치가 높은 순으로 높은 효율의 곡괭이를 사용하게끔 코드를 작성했다.


*****
