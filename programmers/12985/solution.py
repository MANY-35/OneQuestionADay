def solution(n,a,b):
    
    i = 0
    while(a != b):
        i += 1
        if a > 1:
            a = a//2 + a%2
        if b > 1:
            b = b//2 + b%2

    return i