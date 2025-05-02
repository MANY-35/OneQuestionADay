# Lv2 [1차] 캐시

### 1차 시도 (성공)
```py
def solution(cacheSize, cities):
    answer = 0
    myCache = []
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    
    for city in cities:
        if city in myCache:
            index = myCache.index(city)
            myCache = myCache[:index] + myCache[index+1:]
            answer += 1
        else:
            answer += 5

        myCache.append(city)
        if len(myCache) > cacheSize:
            myCache = myCache[1:]
    return answer
```
캐시 교체 알고리즘 LRU를 구현하는 문제였다. LRU를 잊고 살아서 검색해보았다.  
간단하게 리스트에서 검색하여 지우거나 추가하는 방식으로, 가장 앞쪽에 있는 것을 오래된 것이라고 판단하도록 했다.  
처음에 풀었을 당시 대소문자를 구분하지 않는다는 조건을 생각하지 않아서 올바른 답을 내지 못했다.  
>다른 사람들의 풀이를 보니 데크를 이용하여 풀었다면 좀 더 간단하게 코드를 작성할 수 있었을 것이라고 생각했다.