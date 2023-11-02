#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

double dfs(vector<int>& info, vector<vector<int>> &arr, int n, int t, vector<double> &val, double k) {
    
    if (!arr[n].size()) {
        val[n] = k * ((!info[n])+1);
        return val[n];
    }
        

    double s = 0;
    for(int i=0; i<arr[n].size(); i++)   
        s += dfs(info, arr, arr[n][i], t, val, k*0.1);
    s /= ((!info[n]) + 1);
    val[n] = s;
    return s;
}

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer;
    vector<vector<int>> arr(info.size());
    vector<double> data(info.size());


    for (vector<int>t : edges)
        arr[t[0]].push_back(t[1]);
 
    
    dfs(info, arr, 0, 0, data, 1);
    

    for(auto l : data) {
        cout << l << " ";
    }
    cout << endl;
    return answer;
}

int main(void) {

    vector<int> info = {
        0,1,0,1,1,0,1,0,0,1,0
    };
    
    vector<vector<int>> edges = {
        {0,1},{0,2},{1,3},{1,4},{2,5},{2,6},{3,7},{4,8},{6,9},{9,10}
    };

    solution(info, edges);
}