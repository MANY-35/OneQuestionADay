def solution(msg):
    dictionary = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = []
    i=0
    while i < len(msg):
        w = c = msg[i:]
        while w not in dictionary:
            c = w[-1]
            w = w[:-1]

        answer.append(dictionary.index(w)+1)
        dictionary.append(w+c)
        i += len(w)
    
    return answer