s = "aaaaaaaaaaaaaaaaaabab"

def check(s, l, r):
    for i in range(1, (r-l+1)//2+1):
        if s[l+i] != s[r-i]:
            return False
    return True
answer = 0
for l in range(len(s)):
    for r in range(len(s)-1, l-1, -1):
        if s[l] == s[r] and answer < (r-l+1):
            if check(s, l, r):
                answer = r-l+1
print(answer)