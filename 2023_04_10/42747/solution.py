citations = [4, 2, 6, 1, 5]

answer = []
citations.sort(reverse=True)

l = len(citations)
for i in range(l):
    
    print(i+1, citations[i], l-(i+1))
    
    if i+1 >= citations[i] and l-(i+1) < citations[i]:
        answer.append(citations[i])
    
print(answer)