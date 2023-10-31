#include <string>
#include <vector>
#include<iostream>
using namespace std;

long long solution(vector<int> sequence) {
    long long answer = 0;
    int len = sequence.size();

    if (len == 1)
        return (sequence[0] > 0 ? sequence[0] : -sequence[0]);

    vector<int> t(len);
    vector<long long> arr(len);

    for(int i=0, flag=1; i<len; i++) {
        t[i] = sequence[i] * flag;
        flag = -flag;
    }

    for (int flag : {1, -1}) {
        arr[0] = t[0] * flag;
        int index = 0;
        for(int i=1; i<len; i++) {
            if (arr[i-1] + (t[i] * flag) < (t[i]*flag)) {
                arr[i] = (t[i] * flag);
            } else {
                arr[i] = arr[i-1] + (t[i] * flag);
            }   
            if (arr[i] > answer)
                answer = arr[i];
        }
    }
    return answer;
}

int main(void) {
    vector<int> sequence = {
        2, 3, -6, 1, 3, -1, 2, 4
    };

    cout << solution(sequence) << endl;
}
