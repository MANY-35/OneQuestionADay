import re
from itertools import permutations
expression = "100-200*300-500+20"




priorities = list(permutations("+-*", 3))
t = re.split('([+|*|-])', expression)
numbers = [int(i) for i in t[0::2]]
operators = [i for i in t[1::2]]


max = 0
for priority in priorities:
    num = numbers.copy()
    op = operators.copy()
    print(priority)
    for ch in priority:
        
        index = []
        for i in range(len(op)):
            if ch == op[i]:
                index.append(i)
    
        while index:
            i = index.pop(0)
            if ch == "+":
                num[i] += num[i+1]
            elif ch == '-':
                num[i] -= num[i+1]
            else:
                num[i] *= num[i+1]           
            num.pop(i+1)
            op.pop(i)
            index = [x-1 for x in index]
            
    if num[0] < 0:
        num[0] *= -1
    max = num[0] if max < num[0] else max
print(max)

