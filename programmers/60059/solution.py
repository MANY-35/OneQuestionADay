def turn(arr):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            t[j][-1-i] = arr[i][j]
    return t
def check(arr, answer):
    c = []
    for i in range(len(answer)):
        c.append([])
        for j in range(len(answer)):
            c[-1].append(arr[i][j] + answer[i][j])
    for i in c:
        for j in i:
            if j != 1:
                return False
    return True    

def solution(key, lock):
    answer = [(i,j) for i in range(len(lock)) for j in range(len(lock)) if lock[i][j] == 0]
    xs, xe = len(lock), 0
    ys, ye = len(lock), 0


    print('lock')
    for k in lock:
        print(k)
    print()

    for y, x in answer:
        if xs > x:
            xs = x
        if xe <= x:
            xe = x+1
        if ys > y:
            ys = y
        if ye <= y:
            ye = y+1
    answer = []
    for i in range(ys, ye):
        answer.append([])
        for j in range(xs, xe):
            answer[-1].append(lock[i][j])
    
    print('answer')
    for k in answer:
        print(k)
    print()
    
    for i in range(4):
        print('key')
        for k in key:
            print(k)
        print()
        
        for y in range(len(key)-(ye-ys)+1):
            for x in range(len(key)-(xe-xs)+1):
                t = []
                for i in range(y, y+(ye-ys)):
                    t.append([])
                    for j in range(x, x+(xe-xs)):
                        t[-1].append(key[i][j])
                
                print('부분')
                for k in t:
                    print(k)
                print()
                    
                if check(t, answer):
                    return True
        key = turn(key)
    return False


key = [[1,0,0], [1,1,0], [0,0,0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

# 3 7 11 20 24 26 28 30 33 36 37