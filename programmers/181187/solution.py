import math

def f(r):
    count = r
    for i in range(1, r):
        count += math.floor(math.sqrt(r**2 - i**2))
    return count * 4 + 1
def solution(r1, r2):
    c = 0
    for i in range(0, r1):
        k = math.sqrt(r1**2 - i**2)
        if k == math.floor(k):
            c += 1
    c *= 4
    return f(r2) - f(r1) + c


print(solution(5, 10))