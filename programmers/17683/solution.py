# def solution(m, musicinfos):
#     def conversionScal(m:str):
#             scale = ["C#","C","D#", "D", "E", "F#", "F", "G#", "G", "A#", "A", "B"]
#             mash = ["c", "C", "d", "D", "E", "f", "F", "g", "G", "a", "A", "B"]
#             for i in range(len(scale)):
#                 m = m.replace(scale[i], mash[i])
#             return m
#     musicdata = []
#     for data in musicinfos:
#         data = data.split(",")

#         t = data[0].split(":")
#         t1 = int(t[0])*60 + int(t[1])
#         t = data[1].split(":")
#         t2 = int(t[0])*60 + int(t[1])
#         t = t2 - t1    

#         data[-1] = conversionScal(data[-1])
#         realm = ""
#         for i in range(t):
#             realm += data[-1][i%len(data[-1])]

#         musicdata.append([t, data[2], realm])

#     answer = []
#     m = conversionScal(m)
#     for i in range(len(musicdata)):
#         if m in musicdata[i][-1]:
#             answer.append([i] + musicdata[i])
#     if answer == []:
#         return "(None)"
#     return sorted(answer, key= lambda x : (-x[1], x[0]))[0][-2]


def solution(m, musicinfos):
    def conversionScal(m:str):
            scale = ["C#","D#","F#","G#","A#"]
            mash = ["c", "d", "f", "g", "a"]
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

    print(musicdata)
    answer = [0, "(None)"]
    m = conversionScal(m)
    for music in musicdata:
        if m in music[-1]:
            if answer[0] < music[0]:
                answer = music[:2]    
    return answer[-1]
