n = 6
times = [7, 10]


l, r = 0, max(times) * n

def check(times, m, n):
    return n <= sum([m//i for i in times])

while l < r:
    m = (l+r)//2
    l, r = (l, m) if check(times, m, n) else (m+1, r)
print(l)

    