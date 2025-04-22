# LV2 후보키

### 1차시도 (성공)
```py
import itertools as its
def duplicateTest(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True

def is_partial_arr(t1, t2):
    c1 = {x: t1.count(x) for x in t1}
    c2 = {x: t2.count(x) for x in t2}
    for x in t1:
        if x not in c2 or c1[x] > c2[x]:
            return False
    return True

def solution(relation):
    answer = set()
    def func(index, n):
        if len(index) < 1:
            return
        t = [[tuple[j] for j in index] for tuple in relation]
        if duplicateTest(t):
            answer.add(index)
        for index_ in list(its.combinations(index, n-1)):
            func(index_,n-1)
        
    func(tuple(i for i in range(len(relation[0]))), len(relation[0]))
    answer = sorted(answer,key= lambda x:len(x), reverse=True)
    answer.append(())
    a = 0
    for i in range(len(answer)-1):
        for j in range(i+1, len(answer)):
            if is_partial_arr(answer[j], answer[i]):
                break
        if j == len(answer)-1:
            a += 1
    return a
```
> 한번에 성공하긴 했지만 엄청난 시간을 소모했다. 접근하는 방식 부터가 문제가 많았다. 많은 시도를 했지만 도중에 막힌 코드들이 많았다. 결국 데이터베이스에서의 기본키를 설정 할 때 처럼 모든 슈퍼키를 찾고, 그 중에 후보키를 찾는 방식으로 코드를 작성했다. 튜플이 부분 튜플인지 아닌지 검사하는 과정 또한 많은 시간을 소모했다.