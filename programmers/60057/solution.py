def solution(s):
    m = []
    for l in range(1, len(s)+1):
        t = []
        for i in range(0,len(s)-l+1, l):
            t.append(s[i:i+l])
        t.append(s[i+l:])

        c = 0
        k = ""
        for i in range(0, len(t)-1):
            if t[i] == t[i+1]:
                c += 1
            else:
                if c>0:
                    k += str(c+1) + t[i]
                else:
                    k+= t[i]
                c = 0
        k += t[-1]
        m.append(len(k))
    
    return sorted(m)[0]