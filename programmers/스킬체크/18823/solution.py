def solution(wallet, bill):
    answer = 0
    lw, sw = max(wallet), min(wallet)
    lb, sb = max(bill), min(bill)
    while lb > lw or sb > sw:
        lb //= 2
        answer += 1
        if sb > lb:
            t = sb
            sb = lb
            lb = t
    return answer

solution([50, 50], [100, 241])