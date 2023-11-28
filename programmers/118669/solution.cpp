#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <queue>

using namespace std;
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
        if(func(arr, p.first, e, max(m, p.second), arr[p.first], vist))
            return max(m, p.second);
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

int main(void) {
    int n = 7;

    vector<vector<int>> paths = {
        {1, 4, 4},
        {1, 6, 1},
        {1, 7, 3},
        {2, 5, 2},
        {3, 7, 4},
        {5, 6, 6},
    };

    vector<int> gates = {
        {1}
    };

    vector<int> summits = {
        {2,3,4}
    };
    
    auto answer = solution(n, paths, gates, summits);
    for(int i : answer) {
        cout << i << " ";
    }
    cout << endl;
}