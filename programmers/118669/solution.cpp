#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>

using namespace std;

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

int main(void) {
    int n = 6;

    vector<vector<int>> paths = {
        {1, 2, 3},
        {2, 3, 5},
        {2, 4, 2},
        {2, 5, 4},
        {3, 4, 4},
        {4, 5, 3},
        {4, 6, 1},
        {5, 6, 1}
    };

    vector<int> gates = {
        {1, 3}
    };

    vector<int> summits = {
        {5}
    };
    
    auto answer = solution(n, paths, gates, summits);
    for(int i : answer) {
        cout << i << " ";
    }
    cout << endl;
}