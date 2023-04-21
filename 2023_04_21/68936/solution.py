

def solution(arr):
    answer = [0,0]
    def check(arr : list[list]):
        n = arr[0][0]
        for l in arr:
            for e in l:
                if n != e:
                    check([arr[i][:len(arr[i])//2] for i in range(len(arr)//2)])
                    check([arr[i][len(arr[i])//2:] for i in range(len(arr)//2)])
                    check([arr[len(arr)//2 + i][:len(arr[i])//2] for i in range(len(arr)//2)])
                    check([arr[len(arr)//2 + i][len(arr[i])//2:] for i in range(len(arr)//2)])
                    return
        answer[n] += 1
        return
    
    check(arr)
    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))