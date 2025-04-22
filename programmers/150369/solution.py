def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [[i+1, deliveries[i]] for i in range(len(deliveries)) if deliveries[i]]
    pickups = [[i+1, pickups[i]] for i in range(len(pickups)) if pickups[i]]

    while deliveries or pickups:
        i = 0
        if deliveries:
            i = deliveries[-1][0]
        j = 0
        if pickups:
            j = pickups[-1][0]
        answer += max(i, j) * 2    
        
        stack = 0
        while stack < cap and deliveries:
            last = deliveries.pop()
            stack += last[1]
        if stack > cap:
            deliveries.append([last[0], stack-cap])

        stack = 0
        while stack < cap and pickups:
            last = pickups.pop()
            stack += last[1]
        if stack > cap:
            pickups.append([last[0], stack-cap])
            
    return answer


solution(2, 2, [0, 0], [0, 4])