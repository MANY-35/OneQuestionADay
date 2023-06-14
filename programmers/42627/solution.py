import heapq
def solution(jobs):
    t = sorted(jobs, key=lambda x:x[0], reverse=True)
    k = t.pop()
    arr = [(k[1], k[0])]
    answer = 0
    time = arr[0][1]
    while True:
        if t == [] and arr == []:
            return answer//len(jobs)
        while t:
            if t[-1][0] <= time:
                m = t.pop()
                heapq.heappush(arr, (m[-1], m[0]))
            else:
                break
        if arr:
            n = heapq.heappop(arr)
            answer += (time-n[1])+n[0]
            time += n[0]
        else:
            time += 1
    return answer//len(jobs)