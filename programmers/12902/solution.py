def solution(n):
    if n % 2:
        return 0
    a = n // 2
    arr = [0 for _ in range(a+1)]
    arr[1] = 3
    for i in range(1, a):
        j = 0
        c = 2
        while (j+1)*(i+1) <= a:
            arr[(j+1)*(i+1)] += c
            c *= 2
            j+=1
    print(arr)
    for i in range(1, len(arr)):
        arr[i] += arr[i-1] * 3
        arr[i] %= 1000000007
    print(arr)
    print(arr[a])
    return arr[a]

solution(6)

# 2 = 3
# 4 = 3 * 3 + 2
# 6 = (3 * 3 + 2) * 3 + 2
# 8 = 



def solution(n):
    if n==2:
        return 3
    if n==4:
        return 11
    answer = 0
    n/=2
    n-=2
    c=(3,11)
    while n>0:
        c=(c[1],c[1]*4-c[0])
        n-=1
    return c[1]%1000000007