#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> checking(vector<int> &info, vector<vector<int>> &arr, int n) {
    queue<int> que;
    vector<int> count(2,0);

    que.push(n);
    while(!que.empty()) {
        int now = que.front();
        que.pop();
        ++count[info[now]];
        for(int i=0; i<arr[now].size(); i++)
            que.push(arr[now][i]);
    }
    return count;
}

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer = 0;
    vector<vector<int>> arr(info.size(), vector<int>(0));

    for(vector<int> edge : edges)
        arr[edge[0]].push_back(edge[1]);    
    
    vector<bool> c(arr.size(), true);
    for (int i=0; i<arr.size(); i++) {
        if(!arr[i].size() && info[i])
            c[i] = false;
    }
    
    for(int i=0; i<arr.size(); i++) {
        vector<int> t;
        for(int j=0; j<arr[i].size(); j++) {
            if (c[arr[i][j]])
                t.push_back(arr[i][j]);
        }
        arr[i] = t;
    }
    
    deque<int> nodes;
    nodes.push_back(0);

    int sheep = 0;
    int wolf = 0;
    while(!info[nodes.front()]) {
        sheep++;
        int n = nodes.front();
        nodes.pop_front();
        for(int i=0; i<arr[n].size(); i++) {
            if(info[arr[n][i]])
                nodes.push_back(arr[n][i]);
            else
                nodes.push_front(arr[n][i]);
        }
    }

    vector<vector<int>> sub;
    for (int i=0; i<nodes.size(); i++) {
        vector<int> t = checking(info, arr, nodes[i]);
        if (t[0] >= t[1]) {
            sheep += t[0];
            wolf += t[1];
        } else {
            sub.push_back({i, t[0], t[1]});
        }
    }

    return answer;
}

int main(void) {

    vector<int> info = {
        0,1,0,1,1,0,1,0,0,1,0
    };
    
    vector<vector<int>> edges = {
        {0,1},{0,2},{1,3},{1,4},{2,5},{2,6},{3,7},{4,8},{6,9},{9,10}
    };

    cout << solution(info, edges) << endl;
}