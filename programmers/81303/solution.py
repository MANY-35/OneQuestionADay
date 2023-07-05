n = 8
k = 1
cmd = ['D 2', 'C', 'C', 'D 1', 'C']

karr = [[1,1] for _ in range(n+2)]
karr[0] = [0,1]
karr[-1] = [1,0]
arr = [True for _ in range(n+2)]
last = []
k+=1
for command in cmd:
    c = command.split()
    
    print(k)
    
    if c[0] == 'D':
        for i in range(int(c[1])):
            k += karr[k][1]
        
    elif c[0] == 'U':
        for i in range(int(c[1])):
            k -= karr[k][0]
    
    elif c[0] == 'C':
        arr[k] = False
        last.append(k)

        karr[k-karr[k][0]][1] += karr[k][1]
        karr[k+karr[k][1]][0] += karr[k][0]

        if k + karr[k][1] <= n:
            k += karr[k][1]
        else:
            k -= karr[k][0]   

    elif c[0] == 'Z':
        d = last.pop()
        
        arr[d] = True
        karr[d-karr[d][0]][1] = karr[d][0]
        karr[d+karr[d][1]][0] = karr[d][1]
    print(c, k)
    
    for i in arr:
        print(i, end='\t')
    print()
    for i in karr:
        print(i, end='\t')
    print('\n')
    
answer = ""       
for i in arr[1:-1]:
    if i:
        answer+='O'
    else:
        answer+='X'
print(answer)