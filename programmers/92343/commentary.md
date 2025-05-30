# LV3 양과 늑대

### 1차시도 (실패)
```py
import heapq
def counting(nodes, i):
    nodes[i][0] = nodes[i][1]-1
    if nodes[i][2] == []:
        if nodes[i][1]:
            return 0
        else:
            return -1
    for j in nodes[i][2]:
        nodes[i][0] += counting(nodes, j)
    return nodes[i][0]

def solution(info, edges):
    nodes = {i:[0,f,[]] for i,f in enumerate(info)}
    for p, c in edges:
        nodes[p][2].append(c)
    counting(nodes, 0)
    
    que = [nodes[0]]
    heapq.heapify(que)
    s, w = 0, 0
    while que:
        heapq.heapify(que)
        checker = que.copy()
        temp = []

        while que:
            n = heapq.heappop(que)
            if n[1] == 0:
                s+=1
                for i in n[2]:
                    heapq.heappush(temp, nodes[i])
            elif s > w+1 and n[2] != []:
                w+=1
                for i in n[2]:
                    heapq.heappush(temp, nodes[i])
            else:
                heapq.heappush(temp, n)
        if temp == checker:
            break
        que = temp
    return s
```
현재 노드에서 자식의 양의 개수를 저장하고 heapq로 우선순위를 설정하고 bfs 알고리즘을 응용하여 탐색하도록 코드를 작성해봤다.  
3분의 2정도의 케이스에서 실패했다. 우선 순위를 설정하는 방법이 잘 못된듯 하다.

*****

### 2차시도 (실패)
```py
def counting(nodes, i, n=0):
    nodes[i][1] = 1-nodes[i][0]
    nodes[i][2] = nodes[i][0]
    if nodes[i][3] == []:
        if nodes[i][0]:
            return [0, 1]
        else:
            return [1, 0]
    for j in nodes[i][3]:
        t = counting(nodes, j, n+1)
        nodes[i][1] += t[0]
        nodes[i][2] += t[1]
    return [nodes[i][1], nodes[i][2]]

def solution(info, edges):
    nodes = {i:[f,0,0,[]] for i,f in enumerate(info)}
    for p, c in edges:
        nodes[p][3].append(c)
    counting(nodes, 0, 0)
    
    que = [nodes[0]]
    checker = []
    s, w = 0, 0
    while que != checker:
        checker = que.copy()
        temp = []
        while que:
            n = que.pop()
            if n[0]:
                if n[3]!=[]:
                    if s>w+1:
                        w += 1
                        for i in n[3]:
                            temp.append(nodes[i])
                    else:
                        temp.append(n)
                        
                    break
            else:
                s+=1
                for i in n[3]:
                    temp.append(nodes[i])
        que = sorted(temp+que, key=lambda x:(-x[0],x[1],-x[2]))
    return s
```
우선순위에 여러가지 조건을 추가해보았는데 절반정도의 케이스에서 실패했으며 무한루프에 빠지는 케이스가 존재했다.

*****

### 3차시도 (실패)
```cpp
typedef struct Node {
    int info;
    int SW[2];
    vector<struct Node*> arr;
} node;

node* dfs(node* n) {
    if (n->arr.empty())
        return n;
    for(int i=0; i<n->arr.size(); i++) {
        node* temp = dfs(n->arr[i]);
        for(int j=0; j<2; j++) 
            n->SW[j] += temp->SW[j];
    }
    return n;

}

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer;
    vector<node> data;
    for (int i=0; i<info.size(); i++) {
        node temp;
        temp.info = info[i];
        temp.SW[info[i]] = 1;
        temp.SW[!info[i]] = 0;
        data.push_back(temp);
    }
    
    for (int i=0; i<edges.size(); i++) 
        data[edges[i][0]].arr.push_back(&data[edges[i][1]]);

    dfs(&(data[0]));
    int wolf = 0, sheep = 0;
    deque<node*> que;
    que.push_back(&data[0]);
    while(!que.empty()) {
        node* n = que.front();
        que.pop_front();

        if (n->info == 0) {
            sheep ++;
            for(int i=0; i<n->arr.size(); i++) {
                if(n->arr[i]->info == 0)
                    que.push_front(n->arr[i]);
                else if(n->arr[i]->SW[0] > 0) {
                    que.push_back(n->arr[i]);
                }
            }
        }
        else {
            wolf++;
            if (sheep <= wolf)
                return sheep;

            node* max = n;
            for (int i=0; i<que.size(); i++) {
                node* temp = que.front();
                que.pop_front();
                if (max->SW[0] <= temp->SW[0]) {
                    if(max->SW[0] == temp->SW[0]) {
                        if (max->SW[1] < temp->SW[1]) {
                            que.push_back(temp);
                            continue;
                        }
                    }
                    que.push_back(max);
                    max = temp;
                } else 
                    que.push_back(temp);
            }
            
            for(int i=0; i<max->arr.size(); i++)
                que.push_front(max->arr[i]);
        }
    }
    return answer;
}
```
초심으로 돌아가 링크드 리스트 형식으로 트리를 구성하되, 각 서브 트리 가 가지는 늑대와 양의 갯수를 구해서 저장한뒤 먼저 탐색할 노드의 우선순위를 주는 방식으로 코드를 작성해 봤다.  
하지만 절반 정도의 케이스에서 실패했다.

*****

### 4차시도 (성공)
```cpp
int func(vector<int> &info, vector<vector<int>> &arr, int n, int state, bool vist[], int max) {
    if(vist[state])
        return max;

    vist[state] = true;
    int wolf = 0;
    for(int i=0, s=1; (s<<i)<=state; i++) {
        if(state&(s<<i) && info[i])
            wolf++;
        if (wolf * 2 >= n)
            return max; 
    }

    if (n-wolf > max) 
        max = n - wolf;

    for(int i=0, s=1; (s<<i)<=state; i++) {
        if(state & (s<<i)) {
            for (int j=0; j<arr[i].size(); j++) {
                if (!(state & (1<<arr[i][j]))) {
                    int t = func(info, arr, n+1, state+(1<<(arr[i][j])), vist, max);
                    if (t > max)
                        max = t;
                }
            }
        }
    }
    return max;
}

int solution(vector<int> info, vector<vector<int>> edges) {
    vector<vector<int>> arr(info.size());

    bool vist[1<<17] = {false,};

    for(int i=0; i<edges.size(); i++) 
        arr[edges[i][0]].push_back(edges[i][1]);

    return func(info, arr, 1, 1, vist, 0);   
}
```
> ~~도저히 풀리지 않아 누군가 올린 문답 보고 풀어봤다.~~

코드의 요점은 bitmask로 모든 노드의 번호를 bit의 자릿수로 치환하여 계산하도록 했으며, 방문한 노드들의 집합(= 10진수의 값)을 vist배열에 저장함으로써 모든 경우의 수를 판단할 수 있게된다.
