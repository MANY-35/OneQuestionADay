# def solution(citations):
#     answer = []
#     citations.sort(reverse=True)

#     l = len(citations)+1
#     for i in range(l):
#         c = 0
#         for j in range(i):
#             if citations[j] >= i:
#                 c += 1
#         if c >= i:
#             answer.append(i)
        
#     return answer[-1]


# print(solution([3, 0, 6, 1, 5]))


def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    l = len(citations)
    for i in range(l):
        if citations[i] >= i+1:
            answer = i+1
        
    return answer

