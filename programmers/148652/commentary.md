# LV2 유사 칸토어 비트열

### 1차시도 (실패)
```py
def solution(n, l, r):
    answer = 0
    ar = r 
    m = []
    for _ in range(n):
        m.append(ar)
        ar = ar // 5 + 1
    m.append(1)
    arr = [1]
    for _ in range(n):
        t = []
        ar = m.pop()
        for j in range(ar):
            if arr[j] == 1:
                t.extend([1, 1, 0, 1, 1])
            else :
                t.extend([0, 0, 0, 0, 0])
        arr = t
    for i in range(l, r+1, 1):
        if arr[i-1] == 1:
            answer += 1
    return answer
```
절반정도 케이스에서 시간초과가 발생했다.  
처음에는 순차적으로 치완하면서 풀려고 시도했으나 n의 최대 값이 20이므로 시간이 너무 오래 걸린다고 판단하여 r값을 기준으로 구하고자 하는 비트까지만 계산하는 식으로 접근했다.  
하지만 이 또한 r의 최대값이 5^20 이라는 큰 수 이기 때문에 시간초과가 발생한 것으로 판단 된다.

-----

### 2차시도 (성공)
```py
def solution(n, l, r):
    answer = 0
    l_i, r_i = l-1, r-1
    l_indexes, r_indexes = [l_i], [r_i]
    for _ in range(n-1):
        l_i //= 5
        r_i //= 5
        l_indexes.append(l_i)
        r_indexes.append(r_i)
    l_i, r_i = 0, 0
    t = [1, 1, 0, 1, 1]
    while l_i == r_i and l_indexes:
        if t[l_i%5] == 0:
            return 0
        l_i = l_indexes.pop()
        r_i = r_indexes.pop()
    l_indexes.append(l_i)
    r_indexes.append(r_i)
    l_b = [1, 1, 0, 1, 1] 
    r_b = [1, 1, 0, 1, 1]
    answer = 1
    while l_indexes:
        l_i = l_indexes.pop() % 5
        r_i = r_indexes.pop() % 5
        answer *= 4
        for i in range(l_i):
            if l_b[i] == 1:
                answer -= 1
        for i in range(r_i+1, 5, 1):
            if r_b[i] == 1:
                answer -= 1
        l_b = [1, 1, 0, 1, 1] if l_b[l_i] != 0 else [0, 0, 0, 0, 0]
        r_b = [1, 1, 0, 1, 1] if r_b[r_i] != 0 else [0, 0, 0, 0, 0]
    
    return answer
```

시간을 줄이기 위해 고민하다가 n번째 유사 칸토어 비트열의 1의 개수 = n-1번째 유사 칸토어 비트열의 1의 개수 x 4 의 규칙성을 발견했다.  
이때 n = 0 일때는 [1] , n = 1 일 때는 [1, 1, 0, 1, 1] 임이 자명하므로, n = 2 일때 부터 입력받은 n까지 x 4 를 반복하면 1 ~ 5^n 까지의 1의 개수를 알아 낼 수 있다.  
하지만 우리가 원하는 n번째에서의 l ~ r 까지를 구하기 위해 해당 값을 5로 나누면 n-1번째에서의 l과 r의 위치를 알아 낼 수 있다.  
이를 배열에 저장하여 다시 1 부터 n 까지 반복하면서 1의 개수를 곱해 나아가면서 l과 r이 포함된 배열에서 1의 개수를 빼준다면  
원하는 값을 얻을 수 있다.

>다른 사람의 코드를 보니 재귀함수를 통해 코드를 좀더 간단하게 풀어낼 수 있는 것 같다.
