# LV2 교점에 별 만들기기

### 1차시도 (실패)
```py
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
    l, r = 100000, -100000
    t, b = -100000, 100000
    for i in range(len(line)):
        for j in range(i+1, len(line), 1):
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
```
> 모든 선에 대하여 소수점이 없는 교점을 판별하는 함수를 적용하여 교점을 찾고 모든 점에 대하여 최 좌상단 최 우하단 을 찾고 점들의 위치를 표시하는 방식으로 풀었으나 두개의 케이스에서 실패하고 두개의 케이스에서 시간초과가 발생 했다.
> line의 길이가 1000 이기에 단순 계산으로 O(n^2)으로 해도 충분하다고 판단했는데 시간이 초과 했다는 것이 의아하다.


*****

### 2차시도 (성공)
```py
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
```
> 시간초과가 발생한것에 초점을 두고 보니 교점을 구할 때의 교점의 값이 처음 상정한 최대 최소값을 벗어나서 생기는 문제였다. line의 각 원소가 -100000, 100000 의 범위라는 것은 단순 계산으로 두 선의 교점의 좌표 x 또는 y 가 100000*100000 일수 있다는 것이다. 따라서 처음 최대 최소를 정할때 부터 문제가 발생했다는 것을 알았다. 이를 해결하니 처음 실패했던 케이스와 시간초과 모두 해결되었다.
