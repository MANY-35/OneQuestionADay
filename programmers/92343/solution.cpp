#include <string>
#include <vector>
#include <iostream>
using namespace std;


int Max = 0;
void dfs(vector<vector<int>> &arr, vector<int> &info, int n, vector<int> SW) {

    SW[info[n]]++;
    if (SW[0] <= SW[1])
        return;

    cout << n << " : " << SW[0] << ", " << SW[1] << endl;

    if (Max < SW[0])
        Max = SW[0];

    for(int i=0; i<arr[n].size(); i++) {
        dfs(arr, info, arr[n][i], SW);
    }
}


int solution(vector<int> info, vector<vector<int>> edges) {
    vector<vector<int>> arr(info.size());

    for(int i=0; i<edges.size(); i++) 
        arr[edges[i][0]].push_back(edges[i][1]);
    for(int i=0; i<arr.size(); i++) {
        cout << i << " : ";
        for(int j=0; j<arr[i].size(); j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }  


    dfs(arr, info, 0, {0,0});
    cout << Max << endl;
    
}
int main(void) {

    vector<int> info = {
        0,0,1,1,1,0,1,0,1,0,1,1
    };
    
    vector<vector<int>> edges = {
        {0,1},{1,2},{1,4},{0,8},{8,7},{9,10},{9,11},{4,3},{6,5},{4,6},{8,9}
    };

    cout << solution(info, edges) << endl;
}