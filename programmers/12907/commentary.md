# LV3 거스름돈

### 1차시도 (실패)
```cpp
int solution(int n, vector<int> money) {
    int len = money.size();
    vector<int> count(len);
    int t = n;
    for(int i=len-1; i>=0; --i) {
        count[i] = t / money[i];
        t %= money[i];
    }
    len--;

    int answer = !t;
    while(len) {
        if(count[len] == 0) {
            len--;
            continue;
        }
        t += money[len];
        count[len]--;

        for(int i=len-1; i>=0; --i) {
            count[i] += t / money[i];
            t %= money[i];
        }  
        if (t==0)
            answer++;

    }
    return answer % 1000000007;
}
```
>간단히 생각해서 최대값의 거스름돈을 하나씩 줄여가며 다른 돈을 증가하는 방식으로 해보았으나 하다보니 모든 경우의 수를 거치지않는 문제점을 발견했다.

*****

### 2차시도 (성공)
```cpp
int solution(int n, vector<int> money) {
    vector<int> dp(n+1);

    dp[0] = 1;
    for(int i=0; i<money.size(); i++) {
        for(int j=money[i]; j<dp.size(); j++) {
            dp[j] += dp[j - money[i]];
        }
    }
    return dp[n] % 1000000007;
}
```
> 이전 코드를 이용하여 아무리 고민해도 모든 경우의 수를 돌기에는 효율성 테스트에서 통과할 수 없다는 느낌이 들어서 검색을 통해 DP알고리즘을 적용하면 간단하게 풀린다는 것을 알아냈다. 문제를 보자마자 DP알고리즘을을 떠올릴 수 있도록 더 많은 문제를 풀어봐야 할 것 같다.
이 코드는 간한하게 1~n 까지 배열을 만들고 그 배열에 cost를 이용한 경우의 수를 더해가는 방식으로 작성 했다. 그렇게 되면 임의의 cost를 배열의 index에서 빼면 그 값에 해당하는 index의 값 즉 모든 경우의 수를 더해서 현재 코스트가 추가된 경우의 수를 구할 수 있다. 

*****