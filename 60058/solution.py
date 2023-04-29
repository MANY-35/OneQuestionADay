def check(record):
    f = 0
    for j in record:
        if j == "(":
            f += 1
        else:
            f -= 1
        if f < 0:
            return False
    return True

def solution(record):
    if record == "":
        return ""
    
    o = c = 0    
    u = v = ""
    for i in range(len(record)):
        if record[i] == "(":
            o += 1
        else:
            c += 1
        if o == c:
            break
    u = record[:i+1]
    v = record[i+1:]
    
    if check(u):
        return u + solution(v)
    k = "(" + solution(v) + ")"
    u = k + "".join(['(' if u[i]==")" else ')' for i in range(1, len(u)-1)])
    return u
    
print(solution("()))((()"))

