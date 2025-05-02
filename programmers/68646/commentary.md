# LV3 풍선 터트리기

### 1차시도 (실패)
```cpp
int min(int *p, int start, int end) {
    int m = 1000000000;
    for(int i=start; i<end; i++) {
        if (p[i] < m)
            m = p[i];
    }
    return m;
}
int solution(vector<int> a) {
    int answer = 0;
    int *p = &a[0];
    int reft, right;
    int len = a.size();
    for (int i=0; i<len; i++) {
        reft = min(p, 0, i);
        right = min(p, i+1, len);
        if (reft < a[i] && right < a[i]) {
            continue;
        }
        answer ++;
    }
    return answer;
}
```
자기 자신을 기준으로 왼쪽에 있는 모든 퐁선들에 대해서 가장 작은값을 구하고 마찬가지로 오른쪽에 있는 모든 풍선들중 가장 작은값을 구하여 자기자신과 값을 비교하는 방식으로 문제를 접근했다.  
하지만 주어진 데이터의 량이 많아 시간이 너무 걸린다.  
최솟값을 구하는 방법을 다시 생각해봐야 할 것 같다.

*****

### 2차시도 (실패)
```cpp
int min(int *p, int start, int end) {
    int m = 1000000000;
    for(int i=start; i<end; i++) {
        if (p[i] < m)
            m = p[i];
    }
    return m;
}
int solution(vector<int> a) {
    int answer = 0;
    int lm, rm;
    int *p = &a[0];
    lm = 1000000000;
    int len = a.size();
    rm = min(p, 1, len);
    for (int i=0; i<len; i++) {
        if (lm > a[i])
            lm = a[i];
        if (a[i] == rm)
            rm = min(p, i+1, len);

        if (lm < a[i] && rm < a[i]) {
            continue;
        }
        answer ++;
    }
    return answer;
}
```
왼쪽 값에 해당하는 것을 반복문으로 계속해서 계산하는 것이 아닌 기준점이 바뀌었을때 기준점과의 비교를 통해 반복을 줄이고, 오른쪽 값또한 기준값이 최솟값일 때만 다시 구하게 하였음에도 몇개의 케이스에서 시간이 초과한다.  
오른쪽 값을 구하는 방식을 다시한번 고려해봐야 할 것 같다.

*****

### 3차 시도 (성공) 
```cpp
int min(vector<int> &arr, int end) {
    int m = 0;
    for(int i=0; i<end; i++) {
        if (arr[i] < arr[m])
            m = i;
    }
    return m;
}
int solution(vector<int> a) {
    int answer = 1;
    int lm, rm;
    lm = rm = 1000000000;
    int index = min(a, a.size());

    for(int i=0; i<index; i++) {
        if (a[i] < lm) {
            lm = a[i];
            answer ++;
        }
    }
    for(int i=a.size()-1; i>index; i--) {
        if(a[i] < rm) {
            rm = a[i];
            answer ++;
        }
    }
    return answer;
}
```
기준점의 오른쪽 값에서의 최솟값을 반복해서 구하는 것은 시간상 불가능 하다는 것을 깨닫고 고민해 보았지만 풀리지 않아 검색의 도움을 통해 최솟값을 기준으로 왼쪽과 오른쪽을 검사하면 된다는 사실을 알아냈다.  
더 작은 값을 터트리는 것이 단 한번이기 때문에 결국 최솟값을 기준으로 왼쪽에서의 최솟값과 오른쪽에서의 최솟값이 결국은 남게되며 이때 가장 최솟값과 비교하면 된다.
