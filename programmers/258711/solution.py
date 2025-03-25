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
print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))