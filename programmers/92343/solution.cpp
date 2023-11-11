#include <string>
#include <vector>
#include <iostream>
using namespace std;


int func(vector<int> &info, vector<vector<int>> &arr, int n, int state, bool vist[], int max) {
    if(vist[state])
        return max;

    vist[state] = true;
    
    int wolf = 0;
    for(int i=0, s=1; (s<<i)<=state; i++) {
        if(state&(s<<i) && info[i])
            wolf++;
        if (wolf * 2 >= n)
            return max; 
    }

    if (n-wolf > max) 
        max = n - wolf;

    for(int i=0, s=1; (s<<i)<=state; i++) {
        if(state & (s<<i)) {
            for (int j=0; j<arr[i].size(); j++) {
                if (!(state & (1<<arr[i][j]))) {
                    int t = func(info, arr, n+1, state+(1<<(arr[i][j])), vist, max);
                    if (t > max)
                        max = t;
                }
            }
        }
    }
    return max;
}


int solution(vector<int> info, vector<vector<int>> edges) {
    vector<vector<int>> arr(info.size());

    bool vist[1<<17] = {false,};

    for(int i=0; i<edges.size(); i++) 
        arr[edges[i][0]].push_back(edges[i][1]);

    return func(info, arr, 1, 1, vist, 0);
    
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