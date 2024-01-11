#include<iostream>
#include<vector>
using namespace std;

void dfs(vector<vector<int>> &arr, int now, int cost, vector<int> &times, vector<int> &dist, int &max) {
    for(int i=0; i<arr[now].size(); i++) {
        int nCost = times[arr[now][i]];
        if(dist[arr[now][i]] < nCost + cost) {
            dist[arr[now][i]] = nCost + cost;
            if(max < nCost + cost)
                max = nCost + cost;
            dfs(arr, arr[now][i], nCost + cost, times, dist, max);    
        }
    }
}

int main(void) {
    vector<int> answer;
    int TC;
    cin >> TC;
    while(TC--) {
        int N, K;
        cin >> N >> K;
        vector<int> times;
        for(int i=0, input; i<N; i++) {
            cin >> input;
            times.push_back(input);
        }
        vector<vector<int>> arr(N, vector<int>());
        for(int i=0; i<K; i++) {
            int x, y;
            cin >> x >> y;
            arr[y-1].push_back(x-1);
        } 
        int W;
        cin >> W;
        W--;
        vector<int> dist(N,0);
        int max = times[W];
        dist[W] = times[W];
        dfs(arr, W, times[W], times, dist, max);
        answer.push_back(max);
    }
    for(auto i : answer)
        cout << i << endl;
    return 0;
}