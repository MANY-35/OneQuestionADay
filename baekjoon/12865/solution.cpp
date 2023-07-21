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
    for (; i<arr->size(); i++)
        func(arr, i+1, k, sum+(*arr)[i].first, val + (*arr)[i].second, all);
}
bool compare(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first)
        return a.second > b.second;
    return a.first > b.first;
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
    sort(arr.begin(), arr.end(), compare);
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