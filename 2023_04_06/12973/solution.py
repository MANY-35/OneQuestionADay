def solution(s):
    stack = ['']

    for i in s:
        a = stack.pop()
        if a == i:
            continue
        stack.append(a)
        stack.append(i)

    if len(stack) > 1:
        return 0
    return 1