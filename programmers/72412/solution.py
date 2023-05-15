import bisect

def solution(info, query):
    board = {}
    for j0 in ['cpp', 'java', 'python', '-']:
        for j1 in ['backend', 'frontend', '-']:
            for j2 in ['junior', 'senior', '-']:
                for j3 in ['chicken', 'pizza', '-']:
                    board[j0+j1+j2+j3] = []
    for i in info:
        arr = i.split(" ")
        for j0 in [arr[0], '-']:
            for j1 in [arr[1], '-']:
                for j2 in [arr[2], '-']:
                    for j3 in [arr[3], '-']:
                        board[j0+j1+j2+j3].append(int(arr[-1]))
    for i in board.values():
        i.sort()
    answer = []
    for q in query:
        arr = q.replace(" and ", "").split()
        t = board[arr[0]]
        answer.append(len(t)-bisect.bisect_left(t, int(arr[-1])))
    return answer
    
info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))