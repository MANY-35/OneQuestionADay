# [골드5] 평범한 배낭

### 1차 시도 (실패)
```cpp
#include <iostream>
#include <set>
#include <utility>
using namespace std;

int main(void) {
    int n,k;
    cin >> n >> k;
    set<pair<int, int>> arr;

    int N = n;
    while(N--){
        int w, v;
        cin >> w >> v;
        arr.insert(pair<int, int>(-w,v));
    }

    int answer = 0;
    for(int i=0; i<n; i++){
        int K = k;
        int V = 0;
        for (auto a : arr){
            if(K+a.first >= 0) {
                K += a.first;
                V += a.second;
            }
        }
        if (answer < V)
            answer = V;
        arr.erase(arr.begin());
    }
    cout << answer << endl;
    return 0;
}
```
넣을 수 있는 가장 큰 물건부터 넣으면서 가치를 비교하는 방식으로
탐욕법과 비슷한 알고리즘을 가지고 풀었다고 생각했으나 실패했다.
물건의 무게와 가치가 정비례할거라는 착각을 한것 같다.

****
### 2차 시도 (실패)
```cpp
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

void combination(int depth, int next, int n, int r, vector<vector<int>> &all, vector<int> t) {
    if (depth == r) {
        all.push_back(t);
        return;
    }
    for (int i=next; i<n; i++){
        t[depth] = i;
        combination(depth+1, i+1, n, r, all, t);
    }
}
int main(void) {
    int n,k;
    cin >> n >> k;
    vector<pair<int, int>> arr;
    int N = n;
    while(N--){
        int w, v;
        cin >> w >> v;
        arr.push_back(pair<int, int>(w,v));
    }
    vector<vector<int>> com;
    for (int i=1; i<=n; i++)
        combination(0, 0, n, i, com, vector<int>(i));
    int answer = 0;
    for (auto c : com){
        int s = 0;
        int v = 0;
        
        for (auto i : c) {
            v += arr[i].first;
            s += arr[i].second;
        }
        if (v <= k && s > answer)
            answer = s;
    }
    cout << answer;
    return 0;
}
```
고민해본 결과 조합을 통해 모든 조합을 확인해야 할 것 같다고 판단하여 조합을구하고
계산해보았지만 정해진 메모리를 초과하는 문제가 발생했다.

****
### 3차 시도 (실패)
```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
void func(vector<pair<int, int>>* arr, int i, int k, int sum, int val, vector<int> *all) {
    if(sum + (*arr)[i].first > k){
        all->push_back(val);
        return;
    }
    for (int j = i; j<arr->size(); j++) {
        if (sum+(*arr)[j].first <= k){
            func(arr, j+1, k, sum+(*arr)[j].first, val + (*arr)[j].second, all);
        }
    }
}
int main(void) {
    int n,k;
    cin >> n >> k;
    vector<pair<int, int>> arr(n);
    int N = n;
    for (int i=0; i<n; i++){
        int w, v;
        cin >> w >> v;
        arr[i] = pair<int, int>(w,v);
    }
    vector<int> all;
    func(&arr, 0, k, 0, 0, &all);

    int max = 0;
    for (auto i:all){
        if (i > max)
            max = i;
    }
    cout << max << endl;

    return 0;
}
```
배열을 n번 탐색하면서 들어올 수 있는 값을 판단해가며 구하는 방식을 생각했으나 뭔가 잘못된 것이 있는것 같다.

****
### 4차 시도 (실패)
```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
void func(vector<pair<int, int>>* arr, int i, int k, int sum, int val, vector<int> *all) {
    if(sum + (*arr)[i].first > k){
        all->push_back(val);
        return;
    }
    for (int j = i; j<arr->size(); j++) {
        if (sum+(*arr)[j].first <= k){
            func(arr, j+1, k, sum+(*arr)[j].first, val + (*arr)[j].second, all);
        }
    }
}
int main(void) {
    int n,k;
    cin >> n >> k;
    vector<pair<int, int>> arr(n);
    int N = n;
    for (int i=0; i<n; i++){
        int w, v;
        cin >> w >> v;
        arr[i] = pair<int, int>(w,v);
    }
    vector<int> all;
    func(&arr, 0, k, 0, 0, &all);

    int max = 0;
    for (auto i:all){
        if (i > max)
            max = i;
    }
    cout << max << endl;

    return 0;
}
```
시간을 초과했다. 재귀함수를 너무 많이 들어가는 것이 문제인것 같다. 이전코드에서 all 변수를 넣었을때,
메모리 초과가 발생해서 static 변수를 이용하여 바꿔봣는데도 실패했다.
****
### 5차 시도 (성공)
```cpp
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
```
도저히 풀리지않아 검색을 통해 dp알고리즘으로 푸는 법을 이용했다.
검색결과 상상하지도 못한 방식으로 문제에 접근하는데,
dp 관련 문제를 지속적으로 풀어봐야 사용하는 감을 익힐 수 있을 것 같다.
