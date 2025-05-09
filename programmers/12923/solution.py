def func(n):
    if n == 1:
        return 0
    l = 1
    i=1
    while i*i<=n:
        i+=1
        if n % i == 0:
            div1 = i
            div2 = int(n/i)
                    
            if div2 <= 10000000:
                return int(div2)
            
            if div1 <= 10000000:
                l = max(l, div1)
    return l
def solution(begin, end):
    answer = []
    for i in range(end-begin+1):
        answer.append(func(begin+i))
    return answer
print(solution(1, 10))