# LV3 등굣길

### 1차시도 (성공)
```py
def solution(m, n, puddles):
    arr = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for p in puddles:
        arr[p[1]][p[0]] = -1
    arr[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j] < 0:
                continue        
            t = arr[i][j]
            if arr[i-1][j] > 0:
                t += arr[i-1][j]
            if arr[i][j-1] > 0:
                t += arr[i][j-1]
            arr[i][j] = t
    return arr[-1][-1] % 1000000007
```
사실 계속 시도했는데 런타임 오류가 발생했다.  
도저히 어느부분이 잘못된지 몰라서 코드를 몇번 갈아 엎었는데도 런타임 오류가 발생해서 질문탭을 보니 물 웅덩이의 x와 y값을 반대로 넣고있었다.
