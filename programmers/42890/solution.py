import itertools as its

def duplicateTest(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True
def is_partial_arr(t1, t2):
    c1 = {x: t1.count(x) for x in t1}
    c2 = {x: t2.count(x) for x in t2}
    for x in t1:
        if x not in c2 or c1[x] > c2[x]:
            return False
    return True

def solution(relation):
    answer = set()
    def func(index, n):
        if len(index) < 1:
            return
        t = [[tuple[j] for j in index] for tuple in relation]
        if duplicateTest(t):
            answer.add(index)
        for index_ in list(its.combinations(index, n-1)):
            func(index_,n-1)
        
    func(tuple(i for i in range(len(relation[0]))), len(relation[0]))
    answer = sorted(answer,key= lambda x:len(x), reverse=True)
    answer.append(())
    a = 0
    for i in range(len(answer)-1):
        for j in range(i+1, len(answer)):
            if is_partial_arr(answer[j], answer[i]):
                break
        if j == len(answer)-1:
            a += 1
    return a