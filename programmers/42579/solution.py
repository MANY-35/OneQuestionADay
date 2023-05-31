def solution(genres, plays):
    l = {}
    for i in range(len(genres)):
        if genres[i] in l.keys():
            l[genres[i]].append([i, plays[i]])
        else:
            l[genres[i]] = [[i,plays[i]]] 
    title = []
    for i in l.keys():
        l[i] = sorted(l[i], key=lambda x:(x[1], -x[0]), reverse=True)
        title.append([i, sum(int(x) for n,x in l[i])])

    title = sorted(title, key=lambda x:x[1],reverse=True)

    answer = []
    for i in title:
        k = l[i[0]][:2]
        for j in k:
            answer.append(j[0])
    return answer