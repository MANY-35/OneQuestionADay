#include<iostream>
#include<vector>
using namespace std;

int main(void) {
    int max = 0;
    vector<int> arr;
    
    int TC;
    cin >> TC;
    while(TC--) {
        int n;
        cin >> n;

        if(n > max)
            max = n;

        arr.push_back(n);
    }
    int DP0[41] = {0,};
    int DP1[41] = {0,};
    DP0[0] = 1;
    DP1[1] = 1;

    for(int i=2; i<=max; i++) {
        DP1[i] = DP1[i-1] + DP1[i-2];
        DP0[i] = DP0[i-1] + DP0[i-2];
    }

    for(auto k : arr)
        cout << DP0[k] << " " << DP1[k] << endl;
    return 0;
}