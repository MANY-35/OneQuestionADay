
def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])
    
    now = -1
    for target in targets:
        if target[0] >= now:
            answer+=1
            now = target[1]

    return answer

solution([[2,4],[1,3],[3,5]])