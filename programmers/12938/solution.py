def solution(n, s):
    arr = [s//n for _ in range(n)]

    for i in range(1, s - sum(arr)+1):
        arr[-i] += 1
    
    if 0 in arr:
        return [-1]
    return arr