# LV2 파일명 정렬

### 1차 시도 (실패)
```py
def Compare(A, B):
    if A['head'] < B['head']:
        return True
    elif A['head'] == B['head']:
        if A['num'] < B['num']:
            return True
    return False
        
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
        FILES.append({'dst' : file, 'head':file[:i].lower(), 'num':num})
    for i in range(len(FILES)):
        for j in range(len(FILES)):
            if Compare(FILES[i], FILES[j]):
                temp = FILES[i]
                FILES[i] = FILES[j]
                FILES[j] = temp
    answer = []
    for file in FILES:
        answer.append(file['dst'])
    return answer
```
> 주어진 데이터 케이스와 그 외 두 개의 데이터 케이스를 제외한 모든 케이스를 실패했다. 도저히 감이 안 온다. 다른 데이터 케이스를 확인해보고 싶다.

*****

### 2차 시도 (실패)
```py
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
        FILES.append({'dst' : file, 'head':file[:i].lower(), 'num':num})
    FILES = sorted(FILES, key=lambda x: x['num'])
    FILES = sorted(FILES, key=lambda x: x['head'])
    return [file["dst"] for file in FILES]
```
> 람다식을 사용하여 기존의 compare 함수 없이 파이썬에서 제공하는 함수를 사용했다. 데이터 케이스 5개를 제외하고 성공했는데, compare 함수를 만들었을 때와 어떤 점이 다른지 아직 잘 모르겠다.

*****

### 3차 시도 (성공)
```py
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
```
> 숫자를 판단할 때 이전 코드에서는 무조건적으로 5글자 중에 숫자를 떼오는 방식으로 생각했는데, 숫자가 나오다가 문자가 나오면 그 순간 number가 종료되어야 한다는 사실을 망각했었다. 그리고 람다식을 조금 수정했다. 그리고 나서 처음 작성한 코드에서도 똑같이 number를 입력받는 코드를 추가했는데도 실패했다. 이유를 아직도 모르겠어서 다시 한번 확인해야 할 필요가 있어 보인다.