def f(x, y):
    code = "0123456789ABCDEF"
    t = []
    while x > 0:
        t.append(code[x%y])
        x //= y
    if t == []:
        return ['0']
    t.reverse()
    return t

def solution(n, t, m, p):
    arr = []
    num = 0
    x = i = 1
    while t > len(arr) :
        target = f(num, n)
        for j in target:
            if i == p + (x-1)*m:
                arr.append(j)
                x += 1
            i += 1 
        num += 1

    answer = ''
    for i in range(t):
        answer += arr[i]
    return answer