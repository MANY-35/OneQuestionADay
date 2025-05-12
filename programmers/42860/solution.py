def displacement(ch):
    t, ch = ord('Z')+1 - ord('A') , ord(ch) - ord('A')
    if t - ch < ch:
        return t - ch
    return ch
    
def solution(name):
    answer = 0
    indexOfA = []
    arr = [[0,0] for _ in range(len(name))]
    for i in range(len(name)):
        if name[i] == 'A':
            indexOfA.append(i)
            continue
        answer += displacement(name[i])
    
    
    
            
    for i in range(len(name)):
        print(name[i], end='\t')
    print()
    for i in arr:
        print(i, end='\t')
        
    
    answer += len(name) - 1
    return answer
print(solution("JEAROAAAAAEN"))