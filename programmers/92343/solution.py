info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
nodes = {i:[f,0,0,[]] for i,f in enumerate(info)}

for p, c in edges:
    nodes[p][3].append(c)
    
def counting(nodes, i, n=0):
    nodes[i][1] = 1-nodes[i][0]
    nodes[i][2] = nodes[i][0]
    if nodes[i][3] == []:
        if nodes[i][0]:
            return [0, 1]
        else:
            return [1, 0]
    for j in nodes[i][3]:
        t = counting(nodes, j, n+1)
        nodes[i][1] += t[0]
        nodes[i][2] += t[1]
    return [nodes[i][1], nodes[i][2]]
counting(nodes, 0, 0)


que = [nodes[0]]
checker = []
s, w = 0, 0
while que != checker:
    checker = que.copy()
    temp = []
    while que:
        n = que.pop()
        if n[0]:
            if n[3]!=[]:
                if s>w+1:
                    w += 1
                    for i in n[3]:
                        temp.append(nodes[i])
                else:
                    temp.append(n)
                break
        else:
            s+=1
            for i in n[3]:
                temp.append(nodes[i])
    que = sorted(temp+que, key=lambda x:(-x[0],x[1],-x[2]))
    print(que)
print(s, w)