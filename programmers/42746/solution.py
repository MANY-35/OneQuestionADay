from functools import cmp_to_key

def strCmp(s1, s2):
    t1 = str(s1)
    t2 = str(s2)
    
    if len(t1) != len(t2):
        temp = t1
        t1 += t2
        t2 += temp
    
    if int(t1) > int(t2):
        return -1
    return 1
    

def solution(numbers):
    answer = ''
    s = sorted(numbers, key=cmp_to_key(strCmp))
    if s[0] == 0:
        return '0'
    
    print(s)
    
    for i in s:
        answer += str(i)
    return answer

print(solution(	[6, 10, 2]))