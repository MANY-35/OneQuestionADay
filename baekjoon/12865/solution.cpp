#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int n,k;
    cin >> n >> k;
    vector<vector<int>> arr(n);
    for (int i=0; i<n; i++){
        int w, v;
        cin >> w >> v;
        arr[i].push_back(w);
        arr[i].push_back(v);
    }

    vector<int> dp(k+1);
    for (int i=0; i<n; i++) {
        for(int j=k; j>=1; j--){
            if(arr[i][0] <= j) {
                dp[j] = max(dp[j], dp[j - arr[i][0]] + arr[i][1]);
            }
        }
    }
    cout << dp.back() << endl;
}