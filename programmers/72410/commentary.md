# LV1 신규 아이디 추천

### 1차시도 (성공)
```py
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
```
간단하게 모든 조건을 진행하는 방식으로 작성했으나 코드가 깔끔하지 못한 것 같다.
>정규식을 이용하면 해결될 것이므로 정규식 공부를 해서 다시 풀어보자.