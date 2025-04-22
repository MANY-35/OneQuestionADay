# LV3 스티커 모으기

### 1차 시도 (성공)
```py
def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)
    
    dp1 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    dp2 = [0] * len(sticker)
    dp2[1], dp2[2] = sticker[1], max(sticker[1], sticker[2])
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    return max(max(dp1), max(dp2))
```
> 며칠 동안 알고리즘적으로 고민하다가 도저히 방법이 떠오르지 않아 검색해보았다.

