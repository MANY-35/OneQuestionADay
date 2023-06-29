board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]


for t, r1, c1, r2, c2, d in skill:
    t = t*2 - 3
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            board[i][j] += (t)*d

answer = 0
for i in board:
    for j in i:
        if j > 0:
            answer += 1
print(answer)