#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

int main(void) {
    double x1, x2, y1, y2;
    double r1, r2;
    vector<int> answer;
    
    int TC;
    cin >> TC;
    while(TC--) {
        cin >> x1 >> y1  >> r1 >> x2 >> y2 >> r2;
        double d;
        d = sqrt(pow(abs(x1-x2),2) + pow(abs(y1-y2),2));
        if(d == 0) {
            if(r1 == r2)
                answer.push_back(-1);
            else
                answer.push_back(0);
        }
        else if(d < abs(r1-r2))
            answer.push_back(0);
        else if(d == abs(r1-r2) || d == r1+r2)
            answer.push_back(1);
        else if(d > r1+r2)
            answer.push_back(0);
        else
            answer.push_back(2);
    }
    for(auto k : answer)
        cout << k << endl;
}