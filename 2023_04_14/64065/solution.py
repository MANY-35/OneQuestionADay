def solution(s):
    n = []
    n = sorted(n, key=lambda x : len(x))
    answer = []
    for i in n:
        for j in answer:
            for k in range(len(i)):
                if i[k] == j:
                    i.pop(k)
                    break
        for j in i:
            answer.append(j)
    
    return [int(x) for x in answer]