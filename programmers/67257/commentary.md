# LV2 두 큐 합 같게하기

### 1차시도 (성공)
``` py
import re
from itertools import permutations
def solution(expression):
    priorities = list(permutations("+-*", 3))
    t = re.split('([+|*|-])', expression)
    numbers = [int(i) for i in t[0::2]]
    operators = [i for i in t[1::2]]

    max = 0
    for priority in priorities:
        num = numbers.copy()
        op = operators.copy()
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
    return max
```
> 숫자와 연산자를 분리하고 그것을 index로 관리하면서 계산하는 방식으로 풀이했다. 
>> 다른 사람들의 풀이를 보니 eval이라는 함수를 사용하는 것을 봣고 이를 이용하면 좀더 파이썬스럽게 풀 수 있을 것 같다.
