from collections import deque
sticker = [14, 6, 5, 11, 3, 9, 2, 10]

a1 = sticker[0]
i = 2
while i < len(sticker)-1:
    if sticker[i] < sticker[i+1]:
        i+=1
        a1 += sticker[i+1]
    else:
        a1 += sticker[i]
    i += 2
if i < len(sticker):
    a1 += sticker[i]

a2 = sticker[1]
i = 3
while i < len(sticker)-1:
    if sticker[i] < sticker[i+1]:
        i+=1
        a2 += sticker[i+1]
    else:
        a2 += sticker[i]
    i += 2
if i < len(sticker):
    a2 += sticker[i]

print(a1, a2)