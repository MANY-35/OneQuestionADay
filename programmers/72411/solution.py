from collections import defaultdict
import itertools

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

menu = defaultdict(int)
for order in orders:
    for i in course:
        for j in list(map("".join, itertools.combinations(order,i))):
            menu["".join(sorted(j))] += 1
menu = {k:v for (k, v) in menu.items() if v >= 2}

answer = []
for c in course:
    s = [menu[i] for i in menu if len(i)==c]
    if s != []:
        m = max(s)
        t = sorted([i for i in menu if len(i)==c and menu[i]==m])
        answer += t
print(sorted(answer))