#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int abs(int a) {
    if (a > 0)
        return a;
    return -a;
}
string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";
    int ud = 0, lr = 0;
    ud = r - x;
    lr = c - y;
    int sum = abs(ud) + abs(lr);
    if (sum > k || (k-sum)%2 != 0)
        return "impossible";

    while (x < r) {
        answer += "d";
        x++;
        k--;
    }
    while (y > c) {
        answer += "l";
        y--;
        k--;
    }
    while (y < c) {
        answer += "r";
        y++;
        k--;
    }
    while (x > r) {
        answer += "u";
        x--;
        k--;
    }
    string ad = "";
    while(k>0){
        if(x < n) {
            answer += "d";
            ad += "u";
            x++;
        }
        else if(y > 1) {
            answer += "l";
            ad += "r";
            y--;
        }
        else if(y < m) {
            answer += "r";
            ad += "l";
            y++;
        }
        else {
            answer += "u";
            ad = ad + "d";
            x--;
        }
        k-=2;
    }

    sort(ad.begin(), ad.end());
    cout << ad << endl;
    return answer + ad;
}

int main(void) {
    string a = "dduullrr";
    cout << a << endl;
    sort(a.begin(), a.end());
    cout << a << endl;
    // cout << solution(6, 6, 2, 6, 6, 5, 11) << endl;

}