# LV2 쿼드압축 후 개수 세기

### 1차시도 (성공)
```py
def solution(arr):
    answer = [0,0]
    def check(arr):
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
```
> 재귀 함수를 이용해 각 부분을 4등분을 계속하여 압축이 가능하거나 더이상 쪼갤 수 없을 때 까지 반복하여 0과 1의 개수를 세는 방법으로 풀었다.