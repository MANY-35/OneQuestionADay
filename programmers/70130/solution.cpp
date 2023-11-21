#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

void permutation(map<vector<int>, int> &per, vector<int> &arr, vector<int> t, int c, int n) {
    if(n-t.size() > arr.size()-c)
        return;
    if(t.size() == n) {
        per[t] = 0;
        return;
    }
    for(int i=c; i<arr.size(); i++) {
        t.push_back(arr[i]);
        permutation(per, arr, t, i+1, n);
        t.pop_back();
    }
}

bool checkStar(vector<int> arr) {
    map<int, int> t;
    int max = 0;
    for(int i=0; i<arr.size(); i+=2) {
        if(arr[i] == arr[i+1])
            return false;
        for (int j=0; j<2; j++) {
            t[arr[i+j]]++;
            if(max < t[arr[i+j]])
                max = t[arr[i+j]];
        }
    }
    if (arr.size()/2 == max)
        return true;
    return false;
}

int solution(vector<int> a) {
    if (a.size() < 2)
        return 0;
    else if(a.size() == 2) {
        if(a[0] == a[1])
            return 0;
        else
            return 2;
    }

    int i = 2;
    while(i+2 <= a.size())
        i+=2;

    for(; i > 2; i-=2) {
        map<vector<int>, int> p = {};
        permutation(p, a, {}, 0, i);
        for(auto k : p) {
            if (checkStar(k.first))
                return i;
        }
    }
    return 0;
}

int main(void) {
    vector<int> a = {0, 3, 0, 3, 3, 2, 3, 2, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3};
    cout << solution(a) << endl;
    
}   