# [브론즈4] 뉴턴과 사과

### 1차 시도 (성공)
```cpp
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
```
사람의 크기가 0으로 수렴한다고 가정하기에 사과의 원점의 좌표중 x 값이 같은 사람만 구하면되는 간단한 문제였다.
