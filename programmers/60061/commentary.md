# LV3 기둥과 보 설치

### 1차시도 (실패)
```py
def solution(n, build_frame):
    arr = [[-1]*(n*2+1)for _ in range(n*2+1)]
    def checker(l):
        x, y, a = l
        if a:
            if arr[y-1][x-1] == 0 or arr[y-1][x+1] == 0 or (arr[y][x-2] == 1 and arr[y][x+2] == 1):
                return True
        else:
            if y == 0:
                return True
            elif arr[y-2][x] == 0 or arr[y-1][x-1] == 1 or arr[y-1][x+1] == 1:
                return True

        return False
    for x, y, a, b in build_frame:
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
                y = 2*y-1
                x = 2*x+1

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
                t.append([x, y+2, 0])            

                if not all(list(map(checker, t))):
                    arr[y][x] = 0

    answer = []
    for i in range(n*2+1):
        for j in range(n*2+1):
            if arr[i][j] != -1:
                answer.append([j//2, i//2 + i%2, arr[i][j]])
    return sorted(answer, key=lambda x:(x[0],x[1]))
```
기본 테스트케이스에서 통과했으나 그 외의 모든 케이스에서 실패했고, 일부 런타임 에러가 발생함 배열의 범위를 벗어나는 에러인듯하다.

*****

### 2차시도 (성공)
```py
def solution(n, build_frame):
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
    return sorted(answer, key=lambda x:(x[0],x[1],x[2]))
```
이전 코드에서 기둥을 제거하는 부분에서 위에 기둥이 있지 않을때도 검사하는 부분에서 오류가 발생했으며, 배열의 범위를 2n+1에서 3n까지 늘려 배열 범위를 벗어나는 것을 방지했고, 문제에서 주어진 출력 조건의 마지막을 제대로 확인하지 않아 발생한 문제였다.  
또한 원래의 좌표로 돌아올때 계산하는 방식에서 문제를 확인하여 고쳐주었다.