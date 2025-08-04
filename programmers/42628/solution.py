from queue import PriorityQueue
def solution(operations):
    def func(que, entrys, flag=True):
        while not que.empty():
            n = que.get()
            if not entrys[n[1]]:
                if flag:
                    entrys[n[1]] = True
                return n[0]
        return 0
    
    min_heap = PriorityQueue()
    max_heap = PriorityQueue()
    entrys = []
    i = 0
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            min_heap.put((num, i))
            max_heap.put((-num, i))
            i += 1
            entrys.append(False)
        elif op == 'D':
            if num == 1:
                func(max_heap, entrys)
            else:
                func(min_heap, entrys)
    
    return [-func(max_heap, entrys, False), func(min_heap, entrys, False)]

            
print(solution(	["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]))