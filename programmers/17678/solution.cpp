#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    int time = 9 * 60;

    deque<int> timetable_int;
    sort(timetable.begin(), timetable.end());
    for (int i=0; i<=n*m && i < timetable.size(); i++) {
        int temp = 0;
        for (int j=4, c=1; j>=0; j--, c*=10) {
            if(j == 2) {
                c = 6;
                continue;
            }
            temp += ((timetable[i])[j]-'0') * c;
        }
        if (temp <= time + n*t)
            timetable_int.push_back(temp);
    }
    for(int i=0; i<n-1; i++) {
        for (int j=0; j<m; j++) {
            if (timetable_int[0] > time)
                break;
            if (!timetable_int.empty())
                timetable_int.pop_front();
        }
        time += t;
    }

    if (timetable_int.size() >= m) 
        time = timetable_int[m-1] - 1;

    for (int i=0, k=600; i<4; i++, k/=10) {
        if(i == 2){
            k = 10;
            answer += ':';
        }
        answer += (time/k) + '0';
        time %= k;
    }
    return answer;
}

int main(void) {
    int n, t, m;
    
    n = 10;
    t = 1;
    m = 5;
    vector<string> timetable = {"09:00", "09:00", "09:00", "09:00", "09:00"};

    cout << solution(n, t, m, timetable) << endl;

    return 0;
}