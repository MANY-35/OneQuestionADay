def check(times, m, n):
    return n <= sum([m//i for i in times])
def solution(n, times):
    l, r = 0, max(times) * n
    while l < r:
        m = (l+r)//2
        l, r = (l, m) if check(times, m, n) else (m+1, r)
    return l