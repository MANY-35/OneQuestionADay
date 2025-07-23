# LV2 하노이의 탑

### 1차시도 (성공)
```py
def solution(n):
    answer = []
    def hanoi(n, start, end, temp):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n - 1, start, temp, end)
            answer.append([start, end])
            hanoi(n - 1, temp, end, start)
    hanoi(n, 1, 3, 2)    
    return answer
```
너무 유명한 하노이의 탑 알고리즘이다.
*****
