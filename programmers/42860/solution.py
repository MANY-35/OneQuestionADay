def displacement(ch):
    t, ch = ord('Z')+1 - ord('A') , ord(ch) - ord('A')
    if t - ch < ch:
        return t - ch
    return ch

def solution(name):
    answer = 0
    minPath = len(name) - 1
    
    for i in range(len(name)):
        answer += displacement(name[i])
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        if next - i > 1:    
            minPath = min(minPath, i*2 + len(name) - next)
            minPath = min(minPath, (len(name) - next)*2 + i)
    return answer + minPath




print(solution("AACALATLAHABAA")) # 1
# print(solution("GTAASKKAE")) # 1