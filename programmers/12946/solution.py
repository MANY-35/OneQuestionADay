def solution(n):
    answer = []
    def hanoi(n, start, end, temp):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n - 1, start, temp, end)
            answer.append([start, end])
            hanoi(n - 1, temp, end, start)
    hanoi(n, 1, 3, 2)    
    return answer

solution(2)