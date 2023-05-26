def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    answer = 0
    while B:
        if A[-1] < B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            B.pop()
    return answer