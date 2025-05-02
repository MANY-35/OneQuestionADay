# LV3 길 찾기 게임

### 1차시도 (실패)
```py
from collections import deque
def preorder(arr, pre, post):
    if len(arr) < 1:
        return
    n = arr.pop()
    l = deque([])
    r = deque([])
    while arr:
        t = arr.pop()
        if t[1][0] < n[1][0]:
            l.appendleft(t)
        else:
            r.appendleft(t)
    pre.append(n[0]+1)
    preorder(l, pre, post)
    preorder(r, pre, post)
    post.append(n[0]+1)

def solution(nodeinfo):
    arr = list(zip(range(len(nodeinfo)),nodeinfo))
    arr = deque(sorted(arr, key=lambda x:(x[1][1], -x[1][0])))
    pre, post = [], []
    preorder(arr,pre, post)

    return [pre, post]
```
노드를 y축을 1순위로 x축을 2순위로 정렬한 후 함수에서 왼쪽 서브노드와 오른쪽 서브노드를 설정하며 재귀하고 전위와 후위를 저장하도록 코드를 작성했다.  
2개의 케이스에서 런타임 에러가 발생했다. 빈 배열이 생겨서 발생한 오류인지 확인해야 될 것 같다.

*****

### 2차시도 (성공)
```py
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def preorder(arr, pre, post):
    if len(arr) < 1:
        return
    n = arr.pop()
    l = deque([])
    r = deque([])
    while arr:
        t = arr.pop()
        if t[1][0] < n[1][0]:
            l.appendleft(t)
        else:
            r.appendleft(t)
    pre.append(n[0]+1)
    preorder(l, pre, post)
    preorder(r, pre, post)
    post.append(n[0]+1)

def solution(nodeinfo):
    arr = list(zip(range(len(nodeinfo)),nodeinfo))
    arr = deque(sorted(arr, key=lambda x:(x[1][1], -x[1][0])))
    pre, post = [], []
    preorder(arr,pre, post)
    return [pre, post]
```
이전 코드에서 에러가 발생하는 부분을 아무리 봐도 못 찾아서 검색해보니 재귀함수의 깊이가 문제였다. 재귀함수의 깊이를 확장하여 해결했다.