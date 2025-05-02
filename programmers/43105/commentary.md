# LV3 정수삼각형

### 1차시도 (성공)
```py
def solution(triangle):
    for i in range(len(triangle)-1):
        k = []
        for j in range(len(triangle[i])):
            k.append(triangle[i+1][j] + triangle[i][j])
            k.append(triangle[i+1][j+1] + triangle[i][j])

        for l in range(1,len(k)-1, 2):
            k[l] = max(k[l], k[l+1])
        triangle[i+1] = [k[0]] + k[1:-1:2] + [k[-1]]    
    return max(triangle[-1])
```
직전 줄의 데이터를 더하여 중복되는 위치의 값들중 가장 큰값을 새로운 값으로 대치하는 방식으로 풀었다.
