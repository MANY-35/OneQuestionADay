import itertools

def solution(users, emoticons):
    discounts = [90, 80, 70, 60]
    t = []
    for emoticon in emoticons:
        i = emoticon
        t.append([])
        for dis in discounts:
            t[-1].append(int(emoticon * dis)//100)

    max = [0, 0]
    for indexs in itertools.product([0,1,2,3], repeat=len(t)):
        arr = [t[i][indexs[i]] for i in range(len(t))]
        per = [i+1 for i in indexs]

        plus = sum = 0
        for data in users:
            s = 0
            for i in range(len(arr)):
                if data[0]/10 <= per[i]:
                    s+= arr[i]
            if s >= data[1]:
                plus += 1
                s=0
            sum += s

        if max[0] < plus:
            max = [plus, sum]
        elif max[0] == plus and max[1] <= sum:
            max = [plus, sum]
    return max