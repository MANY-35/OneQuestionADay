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
