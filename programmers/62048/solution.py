def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
def solution(w,h):
    X, Y = (h, w) if h>w else (w, h)
    C = gcd(X, Y)
    X, Y =X//C, Y//C

    if X==Y:
        c = X
    else:
        c = X+Y-1
    return int(w*h - (C*c))