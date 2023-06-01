import itertools as it
def solution(user_id, banned_id):
    def check(bans, users, l):
        for i in range(l):
            if len(bans[i]) != len(users[i]):
                return False
            for j in range(len(bans[i])):
                if bans[i][j] == '*':
                    continue
                if bans[i][j] != users[i][j]:
                    return False
        return True

    answer = 0
    for l in list(it.combinations(user_id, len(banned_id))):
        for b in list((it.permutations(banned_id, len(banned_id)))):
            if check(b, l, len(b)):
                answer += 1
                break
    return answer