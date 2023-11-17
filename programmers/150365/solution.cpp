#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


int dis(int x, int y, int r, int c) {
    return ((c > y) ? c-y : y-c) + ((r > x) ? r-x : x-r);
}
string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";
    int sum = dis(x, y, r, c);
    
    cout << sum << endl;

    if (sum > k || (k-sum)%2 != 0)
        return "impossible";
    

    while(x < n && k >= dis(x,y,r,c)) {
        answer += "d";
        k--;
        x++;
    }
    while(k >= dis(x,y,r,c) && k > 0) {
        if(y > 1) {
            answer += "l";
            y--;
        }
        else { 
            answer += "r";
            y++;
        }
        k--;
    }

    while (x < r) {
        answer += "d";
        x++;
    }
    while (y > c) {
        answer += "l";
        y--;
    }
    while (y < c) {
        answer += "r";
        y++;
    }
    while (x > r) {
        answer += "u";
        x--;
    }

    return answer;
}

int main(void) {
    cout << solution(6, 6, 2, 6, 6, 5, 11) << endl;
}
// 6, 6, 2, 6, 6, 5 11 ddddlllllrrrr