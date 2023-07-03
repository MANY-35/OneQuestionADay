from collections import defaultdict, deque

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]


arr = list(zip(range(len(nodeinfo)),nodeinfo))
arr = deque(sorted(arr, key=lambda x:(x[1][1], -x[1][0])))
print(arr)

v = []
def preorder(arr:deque, node):
    if not arr:
        return
    
    t = arr.pop()
    if t[1][1] == node[1][1]:
        arr.appendleft(t)
        t = arr.pop()

    if t[1][0] > node[1][0] or not arr:
        v.append(t)
        preorder(arr, t)
    else:
        r = arr.pop()
        v.append(t)
        preorder(arr, t)
        v.append(r)
        preorder(arr, r)

n = arr.pop()
preorder(arr, n)
print(v)

    
    
    
    
    