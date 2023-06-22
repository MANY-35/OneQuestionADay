from collections import deque
import heapq 


def checkNode(arr, x, y):
    if x < 0 or x >= len(arr) or y < 0 or y >= len(arr) or arr[y][x] == 1:
        return False
    return True
            
def solution(board):
    costArr = [[9999999 for _ in range(len(board))] for _ in range(len(board))]
    costArr[0][0] = 0
    vist = []
    que = deque([(0,0,0,0,0)])
    while que:
        cost, nx, ny, bx, by = que.popleft()
        que = list(que)
        heapq.heapify(que)
        for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
            if checkNode(board, nx+x, ny+y) and (nx+x, ny+y, bx, by) not in vist:
                vist.append((nx+x, ny+y, bx, by))
                c = 1
                if nx+x != bx and ny+y != by:
                    c+= 5
                n = cost+c
                heapq.heappush(que, (n, nx+x, ny+y, nx, ny))
                if n < costArr[ny+y][nx+x]:
                    costArr[ny+y][nx+x] = n
        que = deque(que)
        
        print(nx, ny, bx, by)
        for l in costArr:
            for i in l:
                if i > 999:
                    print(99, end='\t') 
                else:
                    print(i, end='\t') 
            print()
        print()      
                
    return costArr[-1][-1] * 100


board = [
[0,0,1,0,1,1,0,0,0,0],
[0,0,0,0,1,0,1,1,0,1],
[1,0,0,0,0,1,1,0,1,0],
[0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,1,0,1,1],
[0,0,1,0,1,1,0,1,0,1],
[0,1,0,0,1,0,0,0,1,0],
[1,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,0,1,0,0],
[1,0,0,0,0,0,0,0,1,0],]

print(solution(board))