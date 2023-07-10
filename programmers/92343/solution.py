import heapq

info = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

nodes = {i:[0,f,[]] for i,f in enumerate(info)}

for p, c in edges:
    nodes[p][2].append(c)
    
def counting(nodes, i):
    nodes[i][0] = nodes[i][1]-1
    if nodes[i][2] == []:
        if nodes[i][1]:
            return 0
        else:
            return -1
    for j in nodes[i][2]:
        nodes[i][0] += counting(nodes, j)
    return nodes[i][0]
counting(nodes, 0)


que = [nodes[0]]
heapq.heapify(que)
s, w = 0, 0
while que:
    
    heapq.heapify(que)
    checker = que.copy()
    temp = []
    
    while que:
        n = heapq.heappop(que)
        print(n)
        if n[1] == 0:
            s+=1
            for i in n[2]:
                heapq.heappush(temp, nodes[i])
        elif s > w+1 and n[2] != []:
            w+=1
            for i in n[2]:
                heapq.heappush(temp, nodes[i])
        else:
            heapq.heappush(temp, n)
    
    print('late: ',temp)
    if temp == checker:
        break
    que = temp

print(s, w)