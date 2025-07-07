import math

def edge(m, n, a, b):
    mini = 1000**3
    print(abs(b[1]-a[1]))
    for i in range(1, abs(b[1]-a[1])):
        left = math.sqrt(a[0]**2 + i**2) + math.sqrt(b[0]**2 + (abs(b[1]-a[1])-i)**2)
        right = math.sqrt((m-a[0])**2 + i**2) + math.sqrt((m-b[0])**2 + (abs(b[1]-a[1])-i)**2)
        mini = min(left, right, mini)
    print(abs(b[0]-a[0]))
    for i in range(1, abs(b[0]-a[0])):
        bottom = math.sqrt(a[1]**2 + i**2) + math.sqrt(b[1]**2 + (abs(b[0]-a[0])-i)**2)
        top = math.sqrt((n-a[1])**2 + i**2) + math.sqrt((n-b[1])**2 + (abs(b[0]-a[0])-i)**2)
        mini = min(mini, bottom, top)
    return mini ** 2

def corner(a, b):
    s = math.sqrt(a[0]**2 + a[1]**2) + math.sqrt(b[0]**2 + b[1]**2)
    return s**2


def solution(m, n, startX, startY, balls):
    answer = []
    
    ##lt, rt, lb, rb
    arr = [(startX, n-startY), (m-startX, n-startY), (startX, startY), (m-startX, startY)]
    for bx, by in balls:
        print(bx, by, startX, startY)
        brr = [(bx, n-by), (m-bx, n-by), (bx, by), (m-bx, by)]
        mini = (m*n)**3
        for i in range(4):
            if arr[i][0] > brr[i][0] or arr[i][1] > brr[i][1]:
                continue
            if arr[i][0]*brr[i][1] == arr[i][1]*brr[i][0]:
                t = corner(arr[i], brr[i])
                mini = min(t, mini)
            
        mini = min(edge(m, n, (startX, startY), (bx, by)), mini)
        print(mini)
    return answer

solution(10, 10, 3, 7, [[7,7],[2,7]])
# d = (x2-x1)y1 / (y1+y2)
