# LV3 네트워크

### 1차시도 (성공)
```py
def func(root, v, visted):
    visted.append(v)
    for i in range(len(root[v])):
        if root[v][i] == 1 and i not in visted:
            func(root, i, visted)
    return tuple(sorted(visted))

def solution(n, computers):
    k = set()
    for i in range(n):
        k.add(func(computers, i, []))
    return len(k)
```
> 모든 노드를 시작노드로 하여 갈 수 있는 노드들을 저장한 배열을 set에 저장함으로 중복을 제거하고 저장된 모든 라인의 개수가 결국 네트워크의 개수가 된다는 점을 이용했다.