def solution(n, l, r):
    answer = 0
    l_i, r_i = l-1, r-1
    l_indexes, r_indexes = [l_i], [r_i]
    for _ in range(n-1):
        l_i //= 5
        r_i //= 5
        l_indexes.append(l_i)
        r_indexes.append(r_i)
    l_i, r_i = 0, 0
    t = [1, 1, 0, 1, 1]
    while l_i == r_i and l_indexes:
        if t[l_i%5] == 0:
            return 0
        l_i = l_indexes.pop()
        r_i = r_indexes.pop()
    l_indexes.append(l_i)
    r_indexes.append(r_i)
    l_b = [1, 1, 0, 1, 1] 
    r_b = [1, 1, 0, 1, 1]
    answer = 1
    while l_indexes:
        l_i = l_indexes.pop() % 5
        r_i = r_indexes.pop() % 5
        answer *= 4
        for i in range(l_i):
            if l_b[i] == 1:
                answer -= 1
        for i in range(r_i+1, 5, 1):
            if r_b[i] == 1:
                answer -= 1
        l_b = [1, 1, 0, 1, 1] if l_b[l_i] != 0 else [0, 0, 0, 0, 0]
        r_b = [1, 1, 0, 1, 1] if r_b[r_i] != 0 else [0, 0, 0, 0, 0]
    
    return answer
    
