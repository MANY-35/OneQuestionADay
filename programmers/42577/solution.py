

# def check(arr:list):
#     cl = [False for _ in range(10)]
#     for num in arr:
#         t = int(num[0])
#         if cl[t]:
#             return True
#         cl[t] = True
#     return False

# def solution(phone_book):
#     ln = [phone_book]
#     while ln != []:
#         print(ln)
#         temp = []
#         for phone in ln:
#             kind = {str(_) : [] for _ in range(10)}
#             nln = []
#             for num in phone:
#                 if len(num) == 1:
#                     if check(phone):
#                         return False
#                     else:
#                         break
#                 kind[num[0]].append(num[1:])
#                 if len(kind[num[0]]) == 2:
#                     nln.append(num[0])
            
#             for index in nln:
#                 temp.append(kind[index])
#         ln = temp
#     return True


# print(solution(["119", "97674223", "1195524421"]))


def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True
print(solution(["119", "97674223", "1195524421"]))