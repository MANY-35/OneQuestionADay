def solution(people, limit):
    arr = sorted(people, reverse=True)

    i = 0
    while i < len(arr):
        if (arr[i] + arr[-1]) <= limit:
            arr.pop()
        i += 1
        
    return i