from itertools import combinations

def solution(n, q, ans):
    answer = 0
    possible = [True for _ in range(n)]

    que = list(sorted(zip(q, ans), key=lambda x: x[1]))
    l = que.pop()
    if l[0] == 5:
        return 1
    
    que.append(l)
    for i in que:
        if i[1] == 0:
            for j in i[0]:
                possible[j-1] = False
    
    temp = []
    for i in range(n):
        if possible[i] and i+1 not in l[0]:
            temp.append(i+1)

    arr = []
    for t in list(combinations(temp, 5-l[1])):
        for a in list(combinations(l[0], l[1])):
            arr.append(t + a)

    for a in arr:
        l = 0
        for k in que:
            t = 0
            for j in k[0]:
                if j in a:
                    t += 1
            if t != k[1]:
                break
            l += 1
        if l == len(que):
            answer += 1
    return answer

print(solution(10, 	[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))