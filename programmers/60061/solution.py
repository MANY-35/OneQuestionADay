n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

arr = [[-1]*(n*3)for _ in range(n*3)]
def checker(l):
    x, y, a = l
    if a:
        if arr[y-1][x-1] == 0 or arr[y-1][x+1] == 0 or (arr[y][x-2] == 1 and arr[y][x+2] == 1):
            return True
    else:
        if y == 0:
            return True
        elif y == 1:
            if arr[y-1][x-1] == 1 or arr[y-1][x+1] == 1:
                return True
        else:
            if arr[y-2][x] == 0 or arr[y-1][x-1] == 1 or arr[y-1][x+1] == 1:
                return True
    return False

for x, y, a, b in build_frame:
    x += 1
    #설치
    if b:
        #보
        if a:
            y = 2*y-1
            x = 2*x+1
            if checker([x, y, a]):
                arr[y][x] = 1
            
        #기둥 
        else:
            y = 2*y
            x = 2*x
            if checker([x, y, a]):
                arr[y][x] = 0
     
    # 제거
    else:
        #보
        if a:
            x = 2*x+1
            y = 2*y-1

            #기둥 검사
            arr[y][x] = -1
            t1 = [[x+i, y+1, 0] for i in (-1, 1) if arr[y+1][x+i] == 0]
            
            #보 검사
            t2 = [[x+i, y, 1] for i in (-2, 2) if arr[y][x+i] == 1]
            
            if not all(list(map(checker, t1+t2))):
                arr[y][x] = 1
            
        #기둥
        else:
            y = 2*y
            x = 2*x
        
        
            arr[y][x] = -1
            #보 검사
            t = [[x+i, y+1, 1] for i in (-1, 1) if arr[y+1][x+i] == 1]
            
            #기둥 검사
            if arr[y+2][x] == 0:
                t.append([x, y+2, 0])            
            
            if not all(list(map(checker, t))):
                arr[y][x] = 0


answer = []
for i in range(n*3):
    for j in range(n*3):
        if arr[i][j] != -1:
            if arr[i][j]:
                answer.append([(j-3)//2, (i+1)//2, 1])
            else:
                answer.append([(j-2)//2, i//2, 0])
 
print(sorted(answer, key=lambda x:(x[0],x[1],-x[2])))