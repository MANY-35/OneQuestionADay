# [브론즈3] 상금 헌터

### 1차 시도 (성공)
```cpp
#include <iostream>
using namespace std;

int main(void) {
    int season1[6][2] = {{1, 500}, {3, 300}, {6, 200}, {10, 50}, {15, 30}, {21, 10}};
    int season2[5][2] = {{1, 512}, {3, 256}, {7, 128}, {15, 64}, {31, 32}};
    int n;
    cin >> n;
    for(int i=0; i<n; i++) {
        int a, b;
        cin >> a >> b;
        int money = 0;


        for(int j=0; j<6 && a>0; j++) {
            if(a <= season1[j][0]) {
                money += season1[j][1];
                break;
            }
        }
        for(int j=0; j<5 && b>0; j++) {
            if(b <= season2[j][0]) {
                money += season2[j][1];
                break;
            }
        }
        cout << money * 10000 << endl;
    }
}
```

등수를 누적합으로 미리 계산하여 접근하는 방식으로 풀었다.  

