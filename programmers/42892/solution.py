from collections import deque
import sys
sys.setrecursionlimit(10**6)

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

arr = list(zip(range(len(nodeinfo)),nodeinfo))
arr = deque(sorted(arr, key=lambda x:(x[1][1], -x[1][0])))
def preorder(arr:deque, pre, post):
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
    
pre, post = [], []
preorder(arr,pre, post)
print(pre)
print(post)


    
    
    
    
    