# [실버 1] 인형들

### 1차 시도 (실패)
```cpp
#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    int N, K;
    cin >> N >> K;
    int arr[1000];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }
    long double answer = -1;
    for (int i=0; i<=N-K; i++) {
        long double sum = 0;
        long double avr = 0;
        for (int j=0; j<K; j++) {
            sum += arr[i+j];
        }
        avr = sum / K;
        sum = 0;
        for (int j=0; j<K; j++){
            sum += ((long double)arr[i+j]-avr)*((long double)arr[i+j]-avr);
        }
        avr = sum / K;
        if(avr < answer || answer == -1) {
            answer = avr;
        }
    }
    cout << fixed;
    cout.precision(11);
    cout << sqrt(answer) << endl;
}
```

문제를 해석하는데 상당한 어려움이 있었다. 간단하게 N개중 연속된 K개의 숫자들의 표준편차의 최소를 구하는 문제로 해석하여 접근하였으나 실패했다.  
검색해서 나오는 모든 예제에 대해서 정답을 구할 수 있는데 채점하면 통과를 하지 못해서 많은 시간을 쏟았다.

*****

### 2차 시도 (성공)
```cpp
#include <iostream>
#include <cmath>
using namespace std;

long double func(int arr[], int s, int e){
    long double sum = 0;
    long double aver = 0;
    for(int i=s; i<=e; i++) {
        sum += arr[i];
    }
    aver = sum / (e-s+1);
    sum = 0;
    for (int i=s; i<=e; i++) {
        sum += (arr[i]-aver) * (arr[i]-aver);
    }
    aver = sum / (e-s+1);
    return aver;
}

int main(void) {
    int N, K;
    cin >> N >> K;
    int arr[1000];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }
    long double answer = -1;
    for (int i=0; i<=N-K; i++) {
        for (int j=i+K-1; j<N; j++) {
            long double temp = func(arr, i , j);
            if(answer > temp || answer == -1) {
                answer = temp;
            }
        }
    }
    cout << fixed;
    cout.precision(11);
    cout << sqrt(answer) << endl;
}
```

문제를 해석하는 과정에서 주어진 첫번째 예제와 해설
```
입력
5 3
1 2 3 4 5
출력
0.81649658092

첫 번째부터 세 번째까지의 인형을 선택하면 표준편차는 2/3의 양의 제곱근이 되고, 이 때 표준편차가 최소가 된다. 두 번째부터 네 번째까지의 인형을 선택하는 경우와, 세 번째부터 다섯 번째까지의 인형을 선택하는 경우에도 값은 같다.  
```
을 참고하여 당연하게 연속된 K개의 수열에 대해서만 고려하는 것으로 착각하였다.  
문제에서는 ***K개 이상의 수열*** 이라고 명시되어 있었는데 이를 못봐서 생긴 문제였다.

