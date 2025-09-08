# [골드3] ACM Craft

### 1차 시도 (실패)
```cpp
#include <iostream>
#include <vector>
using namespace std;
void dfs (vector<pair<int, vector<int>>> &arr, int now, int cost, int &max, vector<bool> &visited) {
    if (arr[now].second.empty()){
        if (cost + arr[now].first > max) max = cost+arr[now].first;
    }
    for (auto i : arr[now].second) {
        if (!visited[i]){
            visited[i] = true;
            dfs(arr, i, cost+arr[now].first, max, visited);       
        } 
    }
}
int main(void) {
    int TC;
    cin >> TC;
    vector<int> answer;
    while (TC--) {
        int N, K;
        cin >> N >> K;
        vector<pair<int, vector<int>>> arr(N+1);
        for(int i=1; i<N+1; i++) {
            int num;
            cin >> num;
            arr[i].first = num;
        }
        for (int i=0; i<K; i++) {
            int x, y;
            cin >> x >> y;
            arr[y].second.push_back(x);
        }
        
        vector<bool> visited(N+1, false);
        int target, max = 0;
        cin >> target;
        dfs(arr, target, 0, max, visited);
        answer.push_back(max);
    }
    for (auto i : answer) cout << i << endl;
}

```

깊이우선 탐색을 이용하여 타겟으로부터 종단노드 까지 가장 오래 걸리는 길이 정답이라고 판단하여 접근해보았다.  
하지만 몇개의 케이스에서 실패한 것으로 보인다.  


****

### 2차 시도 (성공)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int dfs_dp(vector<pair<int, vector<int>>> &arr, vector<int> &dp, int now) {
    if (dp[now] != -1) {
        return dp[now];
    }
    int max_prereq_time = 0;
    for (int prereq : arr[now].second) {
        max_prereq_time = max(max_prereq_time, dfs_dp(arr, dp, prereq));
    }
    dp[now] = max_prereq_time + arr[now].first;
    return dp[now];
}
int main(void) {
    int TC;
    cin >> TC;
    vector<int> answer;
    while (TC--) {
        int N, K;
        cin >> N >> K;
        vector<pair<int, vector<int>>> arr(N+1);
        for(int i=1; i<N+1; i++) {
            int num;
            cin >> num;
            arr[i].first = num;
        }
        for (int i=0; i<K; i++) {
            int x, y;
            cin >> x >> y;
            arr[y].second.push_back(x);
        }
        int target;
        cin >> target;
        vector<int> dp(N + 1, -1);
        int result = dfs_dp(arr, dp, target);
        cout << result << "\n";
    }
}
```

깊이 우선 탐색에 DP를 접목시켜서 시간초과의 문제를 해결했다.
