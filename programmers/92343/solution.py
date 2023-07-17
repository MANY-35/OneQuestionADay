from collections import deque

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
nodes = [[f,[]] for f in info]

for p, c in edges:
    nodes[p][1].append(c)



def dsf(nodes, i, s, w, que:deque):
    
    if nodes[i][0]:
        if s<=w+1:
            return
        w+=1
    else:
        s+=1
    que.extend(nodes[i][1])
    
    
        
    