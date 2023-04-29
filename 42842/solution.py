def solution(brown, yellow):
    arr = []
    i = 1
    while i*i <= yellow:
        if yellow%i == 0:
            arr.append([i, yellow//i])
        i += 1

    answer = []
    for a in arr:
        sum = (a[0] + a[1] + 2) * 2
        if sum == brown:
            answer = a  
    
    answer.sort(reverse=True)
    return [answer[0]+2, answer[1]+2]