from collections import deque
def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)
    
    q1 = sum(que1)
    q2 = sum(que2)
    qs = q1 + q2
    if qs % 2 != 0:
        return -1
    
    check = 0
    while q1 != q2:
        answer += 1
        if q1 > q2:
            t = que1.popleft()
            que2.append(t)            
            q1 -= t
            q2 += t
        else:  
            t = que2.popleft()
            que1.append(t)         
            q2 -= t
            q1 += t
        
        check += t
        if check >= qs*2:
            return -1
    return answer