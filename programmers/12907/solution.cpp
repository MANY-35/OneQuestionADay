#include <vector>

#include<iostream>
using namespace std;

int solution(int n, vector<int> money) {
    vector<int> dp(n+1);

    dp[0] = 1;
    for(int i=0; i<money.size(); i++) {
        for(int j=money[i]; j<dp.size(); j++) {
            dp[j] += dp[j - money[i]];
        }
    }
    return dp[n] % 1000000007;
}

int main(void) {
    int n = 18;
    vector<int> money = {
        2,5
    };

    cout << solution(n, money) << endl;
}