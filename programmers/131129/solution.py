def solution(target):
    mod_board = set([50])
    for i in range(1, 21):
        mod_board.update([i, i*2, i*3])
    mod_board = list(sorted(mod_board, reverse=True))
    print(mod_board)
    max_count = target // 60
    max_count += (1 if target%60 in mod_board else 2)
    answer = [max_count, 0]
    i = 0
    while i < max_count:
        if (i+1) * 50 > target:
            break
        i+=1
    if (target - i*50) <= 20:
        i+=1
    answer[1] = i
    return answer

# print(solution(143))

one = set([50])
for i in range(1, 21):
    one.update([i, i*2, i*3])
one = list(sorted(one))
two = set([])
for i in range(len(one)):
    for j in range(len(one)):
        two.add(one[i]+one[j])
two = list(sorted(two))
three = set()
for i in range(len(one)):
    for j in range((len(two))):
        three.add(one[i] + two[j])
three = list(sorted(three))
print(three, len(three))