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