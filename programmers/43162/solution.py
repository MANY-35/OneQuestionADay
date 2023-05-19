def func(root, v, visted):
    visted.append(v)
    for i in range(len(root[v])):
        if root[v][i] == 1 and i not in visted:
            func(root, i, visted)

    return tuple(sorted(visted))

def solution(n, computers):
    k = set()
    for i in range(n):
        k.add(func(computers, i, []))

    return len(k)
