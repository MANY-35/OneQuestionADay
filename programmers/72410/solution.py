def solution(new_id : str):
    task = ''
    for c in new_id:
        if c.isalpha() :
            task += c.lower()
        elif c.isdigit() :
            task += c
        elif c in ["-", "_", "."] :
            task += c
    flag = True
    answer = ""
    for c in task:
        if c == '.':
            if flag:
                flag = False
                answer += c
        else:
            answer += c 
            flag = True
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
    if len(answer) > 15:
        answer = answer[0:15]
        if answer.endswith('.'):
            answer = answer[:-1]
    if answer == '':
        answer = 'a'
    for _ in range(len(answer), 3):
        answer += answer[-1]     
    return answer
