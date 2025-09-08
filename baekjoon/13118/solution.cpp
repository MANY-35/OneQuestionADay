#include<iostream>
using namespace std;

int main(void) {
    int p[4];
    int x, y, r;
    for (int i=0; i<4; i++) {
        cin >> p[i];
    }
    cin >> x >> y >> r;

    int answer = 0;
    for (int i=0; i<4; i++) {
        if (p[i] == x)
            answer = i+1; 
    }
    cout << answer << endl;
}