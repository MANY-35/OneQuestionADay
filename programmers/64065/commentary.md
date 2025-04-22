# LV2 튜플

### 1차시도 (성공)
```py
def solution(s):
    n = []
    for a in s.split("},"):
        a = a.replace('{', "")
        a = a.replace('}', "")
        a = a.split(",")   
        n.append(list(a))
    n = sorted(n, key=lambda x : len(x))

    answer = []
    for i in n:
        for j in answer:
            for k in range(len(i)):
                if i[k] == j:
                    i.pop(k)
                    break
        for j in i:
            answer.append(j)

    return [int(x) for x in answer]
```
> 입력받은 튜플들의 길이로 정렬하여 가장 적은 튜플부터 배열에 저장하면서 튜플에서 배열에 있는 값들을 제거하면서 남은 값을 배열에 저장하는 방식으로 풀었다.
>>ps. 다른사람의 풀이를 보고 내가 파이썬의 기능을 잘 이용하지 못한 것 같다.
>>첫 반복문을 n = [a.replace("{","").replace("}","").split(",") for a in s.split("},")] 이런 식의 파이썬문법을 이용하여 풀수 있었으며 3중 반복문도 사용하지 않았어도 됐고 마지막 반복문은 반복을 하지 않는다.
