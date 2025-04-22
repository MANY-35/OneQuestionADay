# LV2 요격 시스템

### 1차시도 (실패)
```py
def solution(targets):
    shoots = []
    targets = sorted(targets, key=lambda x: x[1]-x[0])
    for target in targets:
        flag = True
        for i in range(len(shoots)):
            if target[0] < shoots[i][0] < target[1] or target[0] < shoots[i][1] < target[1]:
                flag = False
        if flag:
            shoots.append(target)            
    return len(shoots)
```
> 단순히 짧은 구간부터 쌓으면서 그 구간과 겹치지 않는 구간인 경우에 새로 분기를 만들고 겹치는 구간인 경우에는 지나가는 식으로 코드를 작성해보았다.
> 그래프의 구간이 0에서 100,000,000으로 너무 넓은 공간을 차지한다는 생각이 들어서 시간으로 때워보자는 생각으로 했지만 targets의 길이가 500,000 이므로 최악의 경우 O(n^2)으로 시간이 너무 오래 걸린다는 것을 간과했다, 이에 몇개의 케이스에서 시간 초과가 발생했으며 또한 몇개의 케이스에서 실패했다.

*****

### 2차시도 (성공)
```py
def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])
    now = -1
    for target in targets:
        if target[0] >= now:
            answer+=1
            now = target[1]
    return answer
```
> targets의 범위 [s, e]에서 e를 기준으로 현재 e의 위치보다 작은 것들은 항상 같은 미사일로 처리가 가능하다는 사실을 알아냈다. 따라서 현재 미사일이 처리 가능한 최대의 e를 구해서 처리하면 간단하게 해결이 가능했다.
