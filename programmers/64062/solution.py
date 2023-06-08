from collections import deque
import random

stones = 	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

# stones = [9, 6, 4, 8, 3, 5, 7, 3, 6, 1, 1, 6, 8, 7, 3, 6, 7, 6, 5, 8]
# k = 8


# 9 8 7 8

def solution(stones, k):
    if k == 1:
        return min(stones)
    arr = deque([])
    answer = 200000001
    for i, s in enumerate(stones):
        if len(arr)<1:
            arr.append([i,s])
        else:
            while arr:
                if arr[-1][1] < s:
                    arr.pop()
                else:
                    break
            arr.append([i,s])
        
        if i < k:
            continue
        
        if arr[0][0] <= i-k:
            arr.popleft() 
            
        
        answer = min(answer, arr[0][1])
    return answer
    

def get(n):
    return [random.randrange(1,10) for _ in range(n)]

print(solution(stones, k))

# for i in range(10):
#     k = random.randrange(2, 25)
#     arr = get(k)
#     k = random.randrange(1, k//2)
#     print(arr, k)
#     print(solution(arr, k))
#     print()
        