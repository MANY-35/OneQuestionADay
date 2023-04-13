files =  ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

def solution(files):
    FILES = []
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                break

        num = "00000"
        for j in range(5):
            if i+j >= len(file):
                break
            if file[i+j].isdigit():
                num += file[i+j]
                num = num[1:]
            else:
                break
        
        FILES.append({'dst' : file, 'head':file[:i].lower(), 'num':num})

    FILES = sorted(FILES, key=lambda x: (x['head'], x['num']))
    return [file["dst"] for file in FILES]

print(solution(files))