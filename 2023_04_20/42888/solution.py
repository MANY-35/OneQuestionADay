def solution(record):
    
    user = {r.split(" ")[1]:r.split(" ")[2] for r in record if len(r.split(" ")) == 3}

    answer = []
    for r in record:
        code = r.split(" ")
        op = code[0]
        id = code[1]

        if op == "Enter":
            answer.append(user[id]+"님이 들어왔습니다.")
        elif op == "Leave":
            answer.append(user[id]+"님이 나갔습니다.")
    
    return answer

