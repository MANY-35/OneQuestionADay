# input data
N= 8
A = [90, 55, 58, 60, 42, 75, 74, 0]
B = [70, 75, 0, 88, 88, 0, 80, 60]
x = 50

x = x/100
Cn = 0
C = []
for i in range(N):
    if A[i] == 0 or B[i] == 0:
        C.append(0)
        Cn += 1
        continue
    C.append(A[i]*x + B[i]*(1-x))


Ct = [C[i] for i in range(len(C)) if C[i] != 0]

N -= Cn
arr = sorted(Ct)

grade = [int(N*0.3), int(N*0.4)]
rank = [[],[],[]]

left = arr[grade[0]]
right = arr[-grade[0]]

print(arr, left, right)
for i in Ct:
    if i >= right:
        rank[0].append(i)
    elif i >= left:
        rank[1].append(i)
    else:
        rank[2].append(i)

print (rank)
for l in range(len(rank)-1):
    rank[l].sort()
    if len(rank[l]) > grade[l]:
        for i in range(len(rank[l])):
            if rank[l][0] != rank[l][i]:
                i-=1
                break
        for j in range(i+1):
            rank[l+1].append(rank[l][0])
            rank[l].pop(0)
print (rank)

answer = ""
for n in C:
    if n == 0:
        answer += 'F'
    elif n in rank[0]:
        answer += 'A'
    elif n in rank[1]:
        answer += 'B'
    else:
        answer += 'C'                 

print(answer)