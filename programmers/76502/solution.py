def f(s):
    a = ['[]', '()', '{}']
    while s != '':
        flag = False
        
        for i in range(len(s)-1):
            if s[i:i+2] in a:
                s = s[:i] + s[i+2:]
                flag = True
                break
        if flag == False:
            break
        
    if len(s) > 0:
        return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if f(s):
            answer += 1
    return answer

print(solution("[](){}"))