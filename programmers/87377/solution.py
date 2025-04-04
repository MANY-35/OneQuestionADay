def myfunc(l1, l2):
    if (l1[0]*l2[1]) - (l1[1]*l2[0]) == 0:
        return False
    
    x1 = l1[1]*l2[2] - l1[2]*l2[1]
    x2 = l1[0]*l2[1] - l1[1]*l2[0]
    
    y1 = l1[2]*l2[0] - l1[0]*l2[2]
    y2 = l1[0]*l2[1] - l1[1]*l2[0]

    if x1 % x2 != 0 or y1%y2 != 0:
        return False
    
    return (x1//x2, y1//y2)
    
def solution(line):
    answer = []
    points = set()
    l, r = 10000000000, -10000000000
    t, b = -10000000000, 10000000000
    for i in range(len(line)):
        for j in range(i, len(line), 1):
            p = myfunc(line[i], line[j])
            if p:
                if r < p[0]:
                    r = p[0]
                if l > p[0]:
                    l = p[0]
                if t < p[1]:
                    t = p[1]
                if b > p[1]:
                    b = p[1]
                points.add(p)
    arr = [["." for i in range(r-l+1)] for j in range(t-b+1)]
    for p in points:
        arr[t-p[1]][p[0]-l] = '*'
    answer = []
    for a in arr:
        answer.append("".join(a))
    return answer