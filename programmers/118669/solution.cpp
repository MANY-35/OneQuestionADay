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
            if(!arr[top[1]][i])
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

    for(int gate : gates) {
        for(int i=0; i<arr.size(); i++) {
            arr[i][gate] = 0;
        }
    }
    for(int summit : summits)
        arr[summit] = vector<int>(n+1, 0);

    for(auto i : arr) {
        for (auto j : i)
            cout << j << " ";
        cout << endl;
    }   

    sort(summits.begin(), summits.end());

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
        if(r < arr[link[l]][l])
            r = arr[link[l]][l];
        l = link[l];
    }
    answer.push_back(r);
    cout << answer[0] << " " << answer[1] << endl;

    return answer;
}

int main(void) {
    int n = 7;

    vector<vector<int>> paths = {
        {1, 6, 1},
        {1, 4, 1},
        {6, 7, 1},
        {6, 2, 1},
        {4, 5, 1},
        {5, 2, 1},
        {2, 3, 1}
    };

    vector<int> gates = {
        {3, 7}
    };

    vector<int> summits = {
        {1, 5}
    };
    
    auto answer = solution(n, paths, gates, summits);
    for(int i : answer) {
        cout << i << " ";
    }
    cout << endl;
}