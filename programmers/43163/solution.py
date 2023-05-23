begin = 'hit'
target = 'cog'
words = ["hot", "lot", "dog", "dot", "log", 'cog']

def checker(str1, str2):
    c = 0
    for i, j in zip(str1, str2):
        if i != j:
            c+=1
    if c > 1:
        return False
    return True
    
    
def func(words, now, target):
    que = [now]
    visted = []
    
    c = 0
    while que:
        t = que.pop()
        c += 1
        for i in words:
            if i not in visted and checker(t, i):
                if i == target:
                    return c
                else:
                    que.append(i)
                    visted.append(i)
    return 0

