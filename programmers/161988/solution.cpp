#include <string>
#include <vector>
#include<iostream>
using namespace std;

long long solution(vector<int> sequence) {
    long long answer = 0;
    int len = sequence.size();
    vector<int> t(len);
    vector<long long> arr(len);

    for(int i=0, flag=-1; i<len; i++) {
        t[i] = sequence[i] * flag;
        flag = -flag;
    }

    for(auto k : t) {
        cout << k << " ";
    }
    cout << endl;

    arr[0] = t[0];
    for(int i=1; i<len; i++) {
        if (arr[i-1] + t[i] < t[i]) {
            arr[i] = t[i];
        } else {
            arr[i] = arr[i-1] + t[i];
        }
        if (arr[i] > answer)
            answer = arr[i];
    }

    for(auto k : arr) {
        cout << k << " ";
    }
    cout << endl;
    
    return answer;
}

int main(void) {
    vector<int> sequence = {
        2, 3, -6, 1, 3, -1, 2, 4
    };

    solution(sequence);
}
