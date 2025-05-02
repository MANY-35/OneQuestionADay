# LV2 불량 사용자

### 1차시도 (실패)
```py
def solution(user_id, banned_id):
    bans = [[] for _ in banned_id]
    for bi in range(len(banned_id)):
        for user in user_id:
            if len(banned_id[bi]) == len(user):
                for i in range(len(banned_id[bi])):
                    if banned_id[bi][i] == '*':
                        continue
                    if banned_id[bi][i] != user[i]:
                        break
                if i == len(banned_id[bi])-1:
                    bans[bi].append(user)

    def func(arr, i, stack=[], result=[]):
        if len(arr) == i:
            result.append(stack.copy())
            return
        for j in range(len(arr[i])):
            stack.append(arr[i][j])
            func(arr, i + 1, stack, result)
            stack.pop()
        return result

    l = func(bans, 0)
    s = set()
    for i in l:
        i = sorted(i)
        if len(set(i)) == len(i):
            s.add("".join(i))
    return len(s)
```
밴된 아이디 목록들에 맞는 아이디들의 리스트를 만들어서 모든 조합을 고려하여 풀어봤으나 두개의 케이스에서 실패했으며 시간초과가 발생한 케이스가 존재했다.

*****

### 2차시도 (성공)
```py
import itertools as it
def solution(user_id, banned_id):
    def check(bans, users, l):
        for i in range(l):
            if len(bans[i]) != len(users[i]):
                return False
            for j in range(len(bans[i])):
                if bans[i][j] == '*':
                    continue
                if bans[i][j] != users[i][j]:
                    return False
        return True

    answer = 0
    for l in list(it.combinations(user_id, len(banned_id))):
        for b in list((it.permutations(banned_id, len(banned_id)))):
            if check(b, l, len(b)):
                answer += 1
                break
    return answer
```
우선 모든 유저들의 조합과 벤된 아이디들의 조합을 비교하는 방식으로 코드를 작성했다.
