def solution(gems):
    dc = {gem:0 for gem in gems}
    left = right = 0
    answer = [0, len(gems)]
    check = set()
    while right < len(gems):
        dc[gems[right]] += 1
        check.add(gems[right])
        if check == dc.keys():
            while dc[gems[left]] > 1:
                dc[gems[left]] -= 1
                left += 1
            if answer[1] - answer[0] > right - left:
                answer = [left, right]
            dc[gems[left]]  -= 1
            check.remove(gems[left])
            left += 1   
        right += 1
    return [answer[0]+1, answer[1]+1]