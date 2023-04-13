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