def solution(triangle):
    for i in range(len(triangle)-1):
        k = []
        for j in range(len(triangle[i])):
            k.append(triangle[i+1][j] + triangle[i][j])
            k.append(triangle[i+1][j+1] + triangle[i][j])

        for l in range(1,len(k)-1, 2):
            k[l] = max(k[l], k[l+1])
        triangle[i+1] = [k[0]] + k[1:-1:2] + [k[-1]]    
    return max(triangle[-1])