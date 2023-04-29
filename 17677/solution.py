def f(x):
    x = [(x[s] + x[s+1]).lower() for s in range(len(x)-1)]
    s = []
    for i in x:
        if i.isalpha():
            s.append(i)
    return s


def solution(str1, str2):
    str1 = f(str1)
    str2 = f(str2)

    n = u = s1 = 0
    for i in str1:
        if i in str2:
            str2.pop(str2.index("{0}".format(i)))
            n += 1
            u += 1
        else:
            s1 += 1

    u += s1 + len(str2)
    if u == 0:
        return 65536
    return int(65536 * n/u)