# LV3 등산코스 정하기

### 1차시도 (실패)
```cpp
#define my_priority_data pair<int, int>, vector<pair<int, int>>, cmp
struct cmp {
    bool operator()(pair<int, int>a, pair<int, int>b) {
        return a.second > b.second;
    }
};

int func(vector<priority_queue<my_priority_data>> &arr, int n, int e, int m, priority_queue<my_priority_data> que, bool vist[]) {
    if (n == e)
        return m;

    if (vist[n])
        return 0;

    vist[n] = true;
    while(!que.empty()) {
        pair<int, int> p = que.top();
        cout << p.first << " " << m  << " " << p.second << endl;
        int re = func(arr, p.first, e, max(m, p.second), arr[p.first], vist);
        if(re)
            return re;
        vist[p.first] = false;
        que.pop();
    }
    return 0;
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    vector<priority_queue<my_priority_data>> arr(n+1);
    for (vector<int> path : paths) {
        arr[path[0]].push(make_pair(path[1], path[2]));
        arr[path[1]].push(make_pair(path[0], path[2]));
    }

    for (int summit : summits)
        arr[summit] = priority_queue<my_priority_data>();
    
    vector<int> m = {0, 10000000};
    for (int summit : summits) {
        for(int gate : gates) {
            bool *vist = new bool[n+1];
            fill_n(vist, n+1, false);
            int k = func(arr, gate, summit, 0, arr[gate], vist);
            cout << k << endl;
            if(m[1] > k) {
                m[0] = summit;
                m[1] = k;
            }
        }
    }
    return m;
}
```
가장 짧은 길로 계속해서 선택해 나가면 가능할 줄 알았으나 아주 잘못 된 방식이었다.

*****

### 2차시도 (실패)
```cpp
struct cmp {
    bool operator()(vector<int> a, vector<int> b) {
        if (a[2] == b[2])
            return a[1] > b[1];
        return a[2] > b[2];
    }
};
int func(vector<vector<int>> &arr, priority_queue<vector<int>, vector<vector<int>>, cmp> &que, vector<int> &summits, vector<int> &link) {
    while(!que.empty()) {
        vector<int> top = que.top();
        que.pop();

        link[top[1]] = top[0];
        for(int summit : summits) {
            if (top[1] == summit)
                return summit;
        }
        
        for(int i=1; i<arr[top[1]].size(); i++) {
            if(arr[top[1]][i] == 0)
                continue;

            if(!link[i])
                que.push({top[1], i, arr[top[1]][i]});
        }
    }
    return -1;
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    vector<vector<int>> arr(n+1, vector<int>(n+1, 0));
    for (vector<int> path : paths) {
        arr[path[0]][path[1]] = path[2];
        arr[path[1]][path[0]] = path[2];
    }
    vector<int> link(n+1, 0);
    priority_queue<vector<int>, vector<vector<int>>, cmp> que;
    for(int gate : gates) {
        link[gate] = -1;
        for(int i=1; i<arr[gate].size(); i++) {
            if(arr[gate][i] != 0)
                que.push({gate, i, arr[gate][i]});
        }
    }
    

    vector<int> answer;
    int l = func(arr, que, summits, link);
    int r = 0;
    answer.push_back(l);
    while(link[l] != -1) {
        if(r < arr[l][link[l]])
            r = arr[l][link[l]];
        l = link[l];
    }
    answer.push_back(r);
    return answer;
}
```
비슷한 방식으로 우선순위 큐에 가장 짧은 길 부터 그려나가면서 현재 노드가 어디에서 왓는지 저장한다.  
그러다가 산정상과 만나면 바로 함수를 종료하고 만난 정상을 알려주고 알아낸 산 정상부터 현재 노드가 정상에 도착할때 만난 노드들을 검사해 나가면서 가장 큰 길의 값을 알아내는 방식으로 해결해 보려 했으나 한개의 실패와 5개의 시간초과가 발생했다.

*****

### 3차시도 (성공)
```cpp
struct cmp {
    bool operator()(vector<int> a, vector<int> b) {
        if (a[2] == b[2])
            return a[1] > b[1];
        return a[2] > b[2];
    }
};
vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    vector<vector<pair<int, int>>> arr(n+1);
    for (vector<int> path : paths) {
        arr[path[0]].push_back({path[1], path[2]});
        arr[path[1]].push_back({path[0], path[2]});
    }
    for(int summit : summits)
        arr[summit] = {};

    vector<pair<int, int>> link(n+1, {0, 0});
    priority_queue<vector<int>, vector<vector<int>>, cmp> que;
    for(int gate : gates) {
        link[gate].first = -1;
        for(pair<int, int> a : arr[gate])
            que.push({gate, a.first, a.second});
    }

    while(!que.empty()) {
        vector<int> top = que.top();
        que.pop();

        if(link[top[1]].second)
            continue;    
        link[top[1]] = {top[0], top[2]};
        for (pair<int, int> i : arr[top[1]]) {
            if(!link[i.first].first)
                que.push({top[1], i.first, i.second});
        }
    }

    priority_queue<vector<int>, vector<vector<int>>, cmp> answer;
    for(int summit : summits) {
        int t = link[summit].first;
        int m = link[summit].second;

        while(t != -1 && t!=0) {
            if(link[t].second > m)
                m = link[t].second;
            t = link[t].first;
        }
        if(t!=0)
            answer.push({0, summit, m});   
    }
    return {answer.top()[1], answer.top()[2]};
}
```
이전 코드처럼 출발지부터 가장 짧은 길들을 연결하는 방식으로 풀었다.  
이전에 틀렷던 케이스는 정상을 만나자마자 종료 해버리는 바람에 같은 값의 길을 가진 더 작은 정상의 번호를 수행하지 않아 생긴 케이스로 이를 해결하기 위해 모든 길을 연결시킨 후 마지막에 값을 체크하는 방식으로 진행했다.  
또한 시간을 줄이기 위해 arr을 n\*n 배열에서
현재 연결 되어 있는 길의 수만큼만 연결되도록 n\*m의 방식으로 바꿧다.
그리고 마지막에 결과를 계산하기 위해서 link의 값을 이전 노드의 위치와 걸리는 시간을 모두 갖도록 변경했다.
> p.s.  
 해설을 작성하다 보니 코드가 더 줄일 수 있는 부분이 발견되어 최대한 줄여서 작성했다.  
 줄이다 보니 link배열 없이도 풀 수 있을 것만 같은 기분이 든다.  
 좀 더 고민해봐야겠다.