import math

def solution(k, d):
    answer = 0
    y = 0
    for y in range(0, d, k):
        answer += int(math.sqrt(d**2 - y**2))//k + 1
    return answer
print(solution(1, 5))
    
    
