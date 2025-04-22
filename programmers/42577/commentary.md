# LV2 전화번호 목록

### 1차시도 (성공)
```py
def check(arr:list):
    cl = [False for _ in range(10)]
    for num in arr:
        t = int(num[0])
        if cl[t]:
            return True
        cl[t] = True
    return False

def solution(phone_book):
    ln = [phone_book]
    while ln != []:
        print(ln)
        temp = []
        for phone in ln:
            kind = {str(_) : [] for _ in range(10)}
            nln = []
            for num in phone:
                if len(num) == 1:
                    if check(phone):
                        return False
                    else:
                        break
                kind[num[0]].append(num[1:])
                if len(kind[num[0]]) == 2:
                    nln.append(num[0])
            
            for index in nln:
                temp.append(kind[index])
        ln = temp
    return True
```
> 기본 베이스는 앞 글자 부터 같은 것 끼리 묶어 나아가는 식으로 풀어보았다. 다시 생각해보면 전체적으로 다소 아쉬운 부분들이 있다. 우선 문자열을 계속 자르는 과정에서 시간이 발생한다는 점이고 마지막 검사하는 부분에서 한번더 반복을통해 검사함으로 시간이 걸린다는 점이다.

*****

> 풀고나서 다른사람의 풀이를 보던 중 해쉬를 이용한 깔끔한 풀이라고 생각하는 코드를 발견했다. 해쉬와 관련된 문제를 더 풀어보는 것이 좋을 것 같다.
>>
```py
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True
```
