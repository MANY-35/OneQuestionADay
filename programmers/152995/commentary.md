# LV3 인사고과

### 1차시도 (실패)
```cpp
int solution(vector<vector<int>> scores) {
    int answer = 1;
    vector<int> *max = &scores[0];
    for (int i=1; i<scores.size(); ++i) {
        int m = (*max)[1] - (*max)[0];
        int t = scores[i][1] - scores[i][0];
        if (m*m <= t*t) {
            if ((*max)[1]*(*max)[0] < scores[i][0]*scores[i][1]) {
                max = &scores[i];
            }
        }
    }
    for(int i=1; i<scores.size(); ++i) {
        if (scores[i][0] < (*max)[0] && scores[i][1] < (*max)[1])
            continue;
        if(scores[0][0] + scores[0][1] < scores[i][0] + scores[i][1])
            answer ++;
    }
    return answer;
}
```
단순하게 좌표평면에서 x,y를 생각하여 그 차가 가장 적은 값을 기준으로 계산을 하면 될 것 같다는 막연한 생각이 들어 작성해 보았으나 당연하게도 절반의 케이스에서 실패했다.  
주어진 데이터가 10만개 여서 하나하나 값을 판단하기엔 너무 오랜 시간이 걸릴 것 같아서 생각한 아이디어 였는데 오류가 있는 것 같다.

*****

### 2차시도 (실패)
```cpp
int solution(vector<vector<int>> scores) {
    int answer = 1;
    vector<bool> arr(scores.size());
    
    for (int i=1; i<scores.size(); ++i) {
        arr[i] = true;
        for (int j=i+1; j<scores.size(); ++j){
            if (scores[i][0] < scores[j][0] && scores[i][1] < scores[j][1]) {
                arr[i] = false;
                break;
            }
        }
    }

    for(int i=1; i<scores.size(); ++i) {
        if(arr[i]) {
            if(scores[i][0] + scores[i][1] > scores[0][0] + scores[0][1])
                answer++;
        }
    }
    return answer;
}
```
혹시 몰라 일일히 가능여부를 판단한 후 계산하는 방식으로 시간 복잡도를 높여보았다.  
시간 초과가 하나의 케이스에서 발생했으나, 절반의 케이스에서 실패가 나왔다.  
알고리즘적으로도 문제가 있는 것 같은데 떠오르는 것이 없다.  
정렬이 되지 않은 상태인데 두번째 반복문을 j=i+1부터 한 것이 문제인 것 같다.

*****

### 3차시도 (실패)
```cpp
int solution(vector<vector<int>> scores) {
    int answer = 1;
    vector<bool> arr(scores.size());
    
    for (int i=0; i<scores.size(); ++i) {
        arr[i] = true;
        for (int j=1; j<scores.size(); ++j){
            if (scores[i][0] < scores[j][0] && scores[i][1] < scores[j][1]) {
                arr[i] = false;
                break;
            }
        }
        if(i==0 && !arr[i])
            return -1;
    }

    for(int i=1; i<scores.size(); ++i) {
        if(arr[i]) {
            if(scores[i][0] + scores[i][1] > scores[0][0] + scores[0][1])
                answer++;
        }
    }
    return answer;
}
```
이전 코드에서 알고리즘적으로 문제가 발생한 부분과 처리하지 않은 예외가 있다는 사실을 알고, 수정을 진행했다.  
하지만 역시 예상한대로 3개의 케이스에서 시간 초과가 발생했다.

*****

### 3차시도 (성공)
```cpp
int solution(vector<vector<int>> scores) {
    int answer = 1;
    vector<int> arr;

    arr.push_back(0);
    for (int i=1, sum=scores[0][0] + scores[0][1]; i<scores.size(); ++i) {
        if (sum < scores[i][0] + scores[i][1])
        {
            arr.push_back(i);
            answer ++;
        }
    }

    for (int i=0; i<arr.size(); ++i) {
         for (int j=1; j<arr.size(); ++j) {
            if(scores[arr[i]][0] < scores[arr[j]][0] && scores[arr[i]][1] < scores[arr[j]][1]) {
                answer --;
                if(i==0)
                    return -1;
                break;
            }
        }
    }
    return answer;
}
```
이전 알고리즘과 비슷한 방식으로 일일히 비교하지만 처음 반복을 통해 가능성이 있는 점수들의 목록을 만들어 반복 횟수를 줄이고자 했다.
>다른 사람들의 풀이를 보니 정렬을 많이 이용하는 것 같다.  
정렬을 이용하여 푸는 방법도 고민을 해보면 좋을 것 같다.