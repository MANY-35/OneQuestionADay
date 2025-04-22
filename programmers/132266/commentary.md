# LV3 부대복귀

### 1차시도 (성공)
```cpp
vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;
    vector<vector<int>> arr(n+1);
    for (auto road : roads) {
        arr[road[0]].push_back(road[1]);
        arr[road[1]].push_back(road[0]);
    }
    
    for (int start : sources) {
        queue<int> que;
        que.push(start);
        vector<bool> visit(n);
        vector<int> dist(n);
        visit[start] = true;
        dist[start] = 0;

        while(!que.empty()) {
            int t = que.front();
            que.pop();
            if (t == destination) {
                answer.push_back(dist[t]);
                que.push(0);
                break;
            }
            for(int i : arr[t]) {
                if (visit[i])
                    continue;
                
                que.push(i);
                visit[i] = true;
                dist[i] = dist[t] + 1;
            }
        }
        if(que.empty()) {
            answer.push_back(-1);
        }
    }
    return answer;
}
```
> 처음 문제를 보자마자 n명의 부대원마다 계산해야해서 플로이드 워셜알고리즘을 이용하여 한번에 모든 계산을하고 값을 출력만하면 될 것이라고 생각했으나 구해야하는 지역의 수가 10만이기 때문에 플로이드 워셜의 O(n^3) 시간으로는 너무 많은 시간이 걸릴 것 같아서 다른 알고리즘을 고민해본 결과 모든길의 가중치가 1이기 때문에 bfs를 이용하여 거리를 구하는 방식으로 작성했다.
> 적다 보니 n명의 부대원이 목적지로 복귀하는것은 역으로 목적지에서부터 n명의 부대원의 거리를 구하는 것과 같다고 문득 떠올랐다. 그렇다면 다익스트라를 통해 목적지에서부터 계산하면 bfs보다 더 빠른 시간과 한번의 계산으로 거리를 구할 수 있을 것이라고 생각된다. 이후 다시 다익스트라를 이용하여 풀어봐야 겠다.