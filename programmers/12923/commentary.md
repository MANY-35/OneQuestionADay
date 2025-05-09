# LV2 숫자 블록록

### 1차 시도 (실패)
```py
def solution(begin, end):
    answer = [1 for _ in range(end-begin+1)]
    if begin == 1:
        answer[0] = 0
    b = begin // 2
    e = end // 2 + 1
    for i in range(b, e):
        if i == 0 or i == 1:
            continue
        j = i
        k = 2
        while j * k <= end:
            if j*k < begin:
                k+=1
                continue
            answer[j*k - begin] = i
            k += 1
    return answer
```
시작점 부터 배수를 구하면서 해당 숫자가 위치할 곳에 체크하는 방식으로 작성했으나, 한 개의 케이스만 성공 했다.  
1부터 100 까지 검수 했는데 어느 부분에서 문제가 생긴 건지 모르겠다.



*****

### 2차 시도 (실패)
```py

def func(n):
    i = n-1
    while i > 0:
        if n % i == 0:
            return(i)
        i-=1
        
def solution(begin, end):
    answer = [1 for _ in range(end-begin+1)]
    k = 0
    if begin == 1:
        answer[0] = 0
        k = 1
    
    for i in range(k, end-begin+1):
        answer[i] = func(begin+i)
    return answer
```
배열을 자세히 살펴 보니 해당 위치의 최대약수를 구하면 될 것 같았다.  
정확성 테스트에서 하나의 케이스를 제외하고 통과하였으나 효율성 테스트에서 시간초과가 발생했다. 

*****

### 3차 시도 (성공)
```py
def func(n):
    if n == 1:
        return 0
    l = 1
    i=1
    while i*i<=n:
        i+=1
        if n % i == 0:
            div1 = i
            div2 = int(n/i)
                    
            if div2 <= 10000000:
                return int(div2)
            
            if div1 <= 10000000:
                l = max(l, div1)
    return l
def solution(begin, end):
    answer = []
    for i in range(end-begin+1):
        answer.append(func(begin+i))
    return answer
```
우선 실패했던 케이스는 문제를 제대로 확인하지 않아 10,000,000 까지의 숫자라는 사실을 놓쳤다.  
또한 시간초과는 이전 O(n^2) 에서 약수를 구하는 함수를 O(root(n))으로 줄여 O(n*root(n)) 까지 줄여서 해결했다.

*****