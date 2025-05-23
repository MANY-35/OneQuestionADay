# LV2 도넛과 막대 그래프

### 1차 시도(실패)
```py
def check_cycle(node_data, start):
    is_8_cycle = False
    if len(node_data[start]) == 0:
        return [False, False]
    elif len(node_data[start]) > 1:
        is_8_cycle = True
    
    now_node = node_data[start][0]
    while True:
        if len(node_data[now_node]) > 1:
            is_8_cycle = True
    
        if node_data[now_node] == []:
            return [False, False]
        elif start in node_data[now_node]:
            return [True, is_8_cycle]
        now_node = node_data[now_node][0]

def solution(edges):
    answer = [0,0,0,0]
    node_data = {}
    random_node = set()
    
    for edge in edges:
        if edge[0] not in node_data:
            node_data[edge[0]] = []
        node_data[edge[0]].append(edge[1])
        if edge[1] not in node_data:
            node_data[edge[1]] = []
        random_node.add(edge[1])
    
    for key in node_data.keys():
        if key not in random_node:
            break
    for i in node_data.pop(key):
        c, e = check_cycle(node_data, i)
        if c:
            if e:
                answer[3] += 1
            else:
                answer[1] += 1    
        else:
            answer[2] += 1
    answer[0] = key
    return answer
```
3개의 케이스에서 실패했고, 몇 개의 케이스에서 시간이 초과되었다. 임의로 추가된 정점을 찾고 그 정점을 통해서 갈 수 있는 그래프가 자기 자신으로 돌아올 수 있는지를 판단하여  
자기 자신으로 돌아온다면 도넛 혹은 8자 모양의 그래프일 것이므로   
1. 진행 과정 중 임의의 노드의 방향이 두 개라면 8자 모양,  
2. 그렇지 않으면 도넛 모양,  
3. 자기 자신으로 돌아오지 못하는 경우에는 막대 그래프  

라고 생각하여 풀었으나 실패했다.

*****

### 2차 시도(실패)
```py
def solution(edges):
    answer = [0,0,0,0]
    node_data = {}
    for edge in edges:
        if edge[0] not in node_data:
            node_data[edge[0]] = {"in":[], "out":[]}
        if edge[1] not in node_data:
            node_data[edge[1]] = {"in":[], "out":[]}
        node_data[edge[0]]["out"].append(edge[1])
        node_data[edge[1]]["in"].append(edge[0])
        
    for key in node_data.keys():
        if node_data[key]["in"] == [] and len(node_data[key]["out"]) > 1:
            answer[0] = key
        elif node_data[key]["out"] == []:
            answer[2] += 1
        elif len(node_data[key]["in"]) + len(node_data[key]["out"]) > 3:
            answer[3] += 1
        elif key in node_data[key]["out"]:
            answer[1] += 1
    return answer
```
굳이 순환해보지 않아도 해당 문제는 이미 완성된 그래프를 임의의 한 점에서 연결한 것이므로 각 정점에서 갈 수 있는 정점과 해당 정점으로 들어오는 정점의 개수를 통해 그래프의 모양을 판단할 수 있다고 생각해서 풀어보았다.  
확실하게 시간은 줄일 수 있었으나 절반 정도의 케이스에서 실패했다.

*****

### 3차 시도(성공)
```py
def what_is_this(node_data, key):
    now = key
    while node_data[now]["c"] == -1:
        now = node_data[now]["out"][0]
        if now == key:
            return 1
    return node_data[now]["c"]
def solution(edges):
    answer = [0,0,0,0]
    node_data = {}
    for edge in edges:
        if edge[0] not in node_data:
            node_data[edge[0]] = {"in":[], "out":[], "c":-1}
        if edge[1] not in node_data:
            node_data[edge[1]] = {"in":[], "out":[], "c":-1}
        node_data[edge[0]]["out"].append(edge[1])
        node_data[edge[1]]["in"].append(edge[0])
    
    for key in node_data.keys():
        if node_data[key]["in"] == [] and len(node_data[key]["out"]) > 1:
            rand_node = key
        elif node_data[key]["out"] == []:
            node_data[key]["c"] = 2
        elif len(node_data[key]["in"]) + len(node_data[key]["out"]) > 3:
            node_data[key]["c"] = 3
    answer[0] = rand_node
    for t in node_data[rand_node]["out"]:
        answer[what_is_this(node_data, t)] += 1
    return answer
```
2차 시도에서 했던 방법에서 길이가 2인 도넛 그래프를 구하는 것이 불가능하여 실패했다는 것을 알게 되었고,  
이를 해결하기 위해 **[ C ]** 라는 값을 추가하여 해당 정점에서 자명하게 알 수 있는 1자 그래프와 8자 그래프임을 나타내 주고   
추가되었다고 판단되는 rand_node에서 순환하며 자명한 정점을 만나면 해당 그래프의 모양을 반환,  
그렇지 않고 순환하여 시작점으로 돌아오면 그것은 도넛 모양인 것으로 판단하여 해당 값을 반환해 주어 결과값에 저장했다.
