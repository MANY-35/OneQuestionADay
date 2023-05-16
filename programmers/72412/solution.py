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
    