#include <iostream>
#include <queue>
#include <vector>
#include <map>
using namespace std;


bool cmp(pair<int, vector<int>> &a, pair<int, vector<int>> &b) {
    if(a.second.size() == b.second.size()) {
        return a.first < b.first;
    }
    return a.second.size() < b.second.size();
}


int main(void) {
    int n, m, x, y;
    cin >> n;
    cin >> m;
    cin >> x;
    cin >> y;

    map<int, vector<int>, cmp> arr;
    map<int, vector<int>>::iterator p;

    for(int i=0, a; i<n; i++) {
        cin >> a; 
        arr[a].push_back(i);
    }
}