# LV2 구명보트

### 1차시도 (성공)
```py
def solution(people, limit):
    arr = sorted(people, reverse=True)

    i = 0
    while i < len(arr):
        if (arr[i] + arr[-1]) <= limit:
            arr.pop()
        i += 1
        
    return i
```
> 최대 2명씩 이라는 키워드가 있어서 생각보다 쉬웠던것 같다. 사람들의 무게를 내림차순으로 정렬하여 무거운 순서대로 탐색하면서 가장 가벼운 사람과 같이 탈 수 있는지 검사하고 탈수 있다면 가장 가벼운 사람을 그 다음 가벼운 사람으로 지정하여 탐색했다.