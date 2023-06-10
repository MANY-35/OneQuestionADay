
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


def solution(stones, k):
    left = 0
    right = max(stones)+1

    def compare(mid):
        return any( len(i)>=k for i in "".join(["T" if i>mid else "F" for i in stones]).split("T"))

    while left<right:
        mid = (left+right)//2
        if compare(mid):
            right = mid
        else:
            left = mid + 1

    return right


print(solution(stones, k))
