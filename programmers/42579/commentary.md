# LV3 베스트 앨범

### 1차시도 (실패)
```py
def solution(genres, plays):
    l = {}
    for i in range(len(genres)):
        if genres[i] in l.keys():
            l[genres[i]].append([i, plays[i]])
        else:
            l[genres[i]] = [[i,plays[i]]] 
    title = []
    for i in l.keys():
        l[i] = sorted(l[i], key=lambda x:x[1], reverse=True)
        title.append([i, l[i][0][1]])
    title = sorted(title, key=lambda x:x[1],reverse=True)
    answer = []
    for i in title:
        k = l[i[0]][:2]
        for j in k:
            answer.append(j[0])
    return answer
```
3분의 2의 테스트에서 실패했다. 조건을 잘못 본것 같다.

*****

### 2차시도 (성공)
```py
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
```
역시나 조건을 잘못보고 판단하여 실패했었다. 조건을 다시 확인하고 코드를 작성하였다.
