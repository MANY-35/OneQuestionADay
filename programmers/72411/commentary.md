# LV2 메뉴 리뉴얼

### 1차시도 (실패)
```py
menu = defaultdict(int)
orders.sort(key=lambda x : len(x), reverse=True)
for i in range(len(orders)-1):
     for j in range(i+1, len(orders)):
         
        print(orders[i], orders[j])
        l = ""
        for k in orders[j]:
            if k in list(orders[i]):
                l += k
        print(l)
        menu[l] += 1
print(menu)
```
가장 긴 문자열부터 문자열의 원소들을 분해하고 탐색하면서 2개이상인 원소들을 추출해 보려 하였으나 원소들을 전부 뽑아내는데 실패함

*****

### 2차 시도(실패)
```py
from collections import defaultdict
def solution(orders, course):
    menu = defaultdict(int)
    for order in orders:
        t = [[i] for i in list(order)]

        for i in range(len(order)):
            for j in range(i, len(order)):
                t[j].append("".join(sorted(order[i] + t[j][-1])))
            t[i].pop()
        for c in sum(sum([],t), []):
            if len(c) in course:
                menu[c] += 1
    answer = []        
    for c in course:
        m = max([menu[i] for i in menu if len(i)==c])
        t = sorted([i for i in menu if len(i)==c and menu[i]==m])
        answer += t
    return answer
```
모든 원소들을 추출하는 과정에서 행렬을 사용하면 된다고 착각하여 행렬을 이용해봤으나 역시 모든 원소를 추출하는 것에 실패함

*****

### 3차시도 (성공)
```py
from collections import defaultdict
import itertools

def solution(orders, course):
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
    return sorted(answer)
```
검색을 통해 combinations 함수를 사용하여 모든 배열의 조합을 구할 수 있다는 사실을 알아냈다.  
그 외의 풀이는 모든 원소의 합을 구하여 가장 많이 사용된 조합을 저장하여 출력하는 방식으로 이전 코드와 비슷하다.  
>다른 사람의 코드를 보고나니 마지막에 계산하는 부분을 조금더 다듬을 수 있을것 같다는 생각이 들었다.
