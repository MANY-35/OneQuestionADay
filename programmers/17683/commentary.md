# LV2 두 큐 합 같게 하기

### 1차 시도 (실패)
```py
def solution(m, musicinfos):
    def conversionScal(m:str):
            scale = ["C#","C","D#", "D", "E", "F#", "F", "G#", "G", "A#", "A", "B"]
            mash = ["c", "C", "d", "D", "E", "f", "F", "g", "G", "a", "A", "B"]
            for i in range(len(scale)):
                m = m.replace(scale[i], mash[i])
            return m
    musicdata = []
    for data in musicinfos:
        data = data.split(",")

        t = data[0].split(":")
        t1 = int(t[0])*60 + int(t[1])
        t = data[1].split(":")
        t2 = int(t[0])*60 + int(t[1])
        t = t2 - t1    

        data[-1] = conversionScal(data[-1])
        realm = ""
        for i in range(t):
            realm += data[-1][i%len(data[-1])]

        musicdata.append([t, data[2], realm])

    answer = []
    m = conversionScal(m)
    for i in range(len(musicdata)):
        if m in musicdata[i][-1]:
            answer.append([i] + musicdata[i])
    if answer == []:
        return "(None)"
    return sorted(sorted(answer, key= lambda x : x[1], reverse=True), key=lambda x:x[0])[0][-2]
```
3개의 케이스에서 실패했다. 어떤 예외에서 처리를 하지 않은 것 같다.

*****

### 2차 시도 (성공)
```py 
def solution(m, musicinfos):
    def conversionScal(m:str):
            scale = ["C#","C","D#", "D", "E", "F#", "F", "G#", "G", "A#", "A", "B"]
            mash = ["c", "C", "d", "D", "E", "f", "F", "g", "G", "a", "A", "B"]
            for i in range(len(scale)):
                m = m.replace(scale[i], mash[i])
            return m
    musicdata = []
    for data in musicinfos:
        data = data.split(",")

        t = data[0].split(":")
        t1 = int(t[0])*60 + int(t[1])
        t = data[1].split(":")
        t2 = int(t[0])*60 + int(t[1])
        t = t2 - t1    

        data[-1] = conversionScal(data[-1])
        realm = ""
        for i in range(t):
            realm += data[-1][i%len(data[-1])]

        musicdata.append([t, data[2], realm])

    answer = []
    m = conversionScal(m)
    for i in range(len(musicdata)):
        if m in musicdata[i][-1]:
            answer.append([i] + musicdata[i])
    if answer == []:
        return "(None)"
    return sorted(answer, key= lambda x : (-x[1], x[0]))[0][-2]
```
마지막 sorted 함수에서 람다식이 내가 생각한 대로 작동하지 않았음을 알아내서 람다식을 수정했다.  
다른 사람의 정답을 보니 처음 코드를 바꿀 때 1:1로 전부 검사하는 것이 아니라 #이 붙은 코드에 대해서만 소문자로 변경해주는 코드가 조금 더 좋아 보인다.  
또한 마지막 맞는 악보를 찾을 때도 전부 저장하여 정렬하는 것보다 탐색할 때 조건을 넣어 저장하는 것이 좋아 보인다.

>## *수정*
>```
>def solution(m, musicinfos):
>    def conversionScal(m:str):
>            scale = ["C#","D#","F#","G#","A#"]
>            mash = ["c", "d", "f", "g", "a"]
>            for i in range(len(scale)):
>                m = m.replace(scale[i], mash[i])
>            return m
>    musicdata = []
>    for data in musicinfos:
>        data = data.split(",")
>        t = data[0].split(":")
>        t1 = int(t[0])*60 + int(t[1])
>        t = data[1].split(":")
>        t2 = int(t[0])*60 + int(t[1])
>        t = t2 - t1    
>
>        data[-1] = conversionScal(data[-1])
>        realm = ""
>        for i in range(t):
>            realm += data[-1][i%len(data[-1])]
>
>        musicdata.append([t, data[2], realm])
>
>    print(musicdata)
>    answer = [0, "(None)"]
>    m = conversionScal(m)
>    for music in musicdata:
>        if m in music[-1]:
>            if answer[0] < music[0]:
>                answer = music[:2]    
>    return answer[-1]
>```