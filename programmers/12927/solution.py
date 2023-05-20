def s1(n, works):
    arr = sorted(works)
    
    for _ in range(n):
        arr[-1] -= 1
        if arr[-1] < 0:
            return 0
        arr = sorted(arr)
    return sum([i*i for i in arr])

def solution(n, works):
    arr = sorted(works, reverse=True)
    s = sum(arr) - n
    if s < 0:
        return 0
    b = []
    while arr:
        s = sum(arr) - n
        t = []
        for i in arr:
            if i > s//len(arr):
                t.append(i)
            else:
                b.append(i)
        if arr == t:
            break
        arr = t
        
    a = [s//len(arr) for _ in range(len(arr))]
    for i in range(s % len(a)):
        a[i] += 1    

    return sum([i*i for i in a] + [i*i for i in b])

works = [2,1,5,4,6]
n = 4
print(s1(n, works))
print(solution(n, works))