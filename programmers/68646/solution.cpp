#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int min(vector<int> &arr, int end) {
    int m = 0;
    for(int i=0; i<end; i++) {
        if (arr[i] < arr[m])
            m = i;
    }
    return m;
}
int solution(vector<int> a) {
    int answer = 1;
    int lm, rm;
    lm = rm = 1000000000;
    int index = min(a, a.size());
    for(int i=0; i<index; i++) {
        if (a[i] < lm) {
            lm = a[i];
            answer ++;
        }
    }
    for(int i=a.size()-1; i>index; i--) {
        if(a[i] < rm) {
            rm = a[i];
            answer ++;
        }
    }
    return answer;
}
int main(void)
{
    vector<int> a;
    a = {
       -16
    };
    
    cout << solution(a);
    return 0;
}