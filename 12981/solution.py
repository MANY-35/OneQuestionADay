def solution(n, words):
    answer = []

    i = 1
    stack = []
    stack.append(words[0])
    for str in words[1:]:
        
        if str in stack:
            break
        
        if stack[-1][-1] != str[0]:
            break 
        
        stack.append(str)
        i += 1
    
    if i == len(words):
        return [0, 0]
    return [(i%n)+1, (i//n)+1]
