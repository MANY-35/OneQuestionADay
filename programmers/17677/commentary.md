# LV2 [1차] 뉴스 클러스터링

### 1차 시도 (성공)
```py
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
```
문자열을 2글자씩 나누고 문자 이외의 값은 버리는 함수를 작성하고, 중복된 문자들을 지워나가는 형식으로 작성하여 풀었다.  
아직 파이썬 문법을 적용하여 푸는 것이 부족하다.  
굳이 함수를 사용하지 않아도 충분히 배열로 만드는 것이 가능했고, 알고리즘적으로도 직접 데이터를 지우면서 확인하지 않아도 가능한 방법이 있다는 것을 인지하지 못했다.
  