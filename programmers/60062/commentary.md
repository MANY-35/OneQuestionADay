# LV3 외벽 점검

### 1차시도 (실패)
```cpp
int answer = 20;
void func(int n, deque<int> weak, vector<int> dist, int deep) {
    if (weak.empty()) {
        if (answer > deep)
            answer = deep;
        return;
    }
    if (dist.empty())
        return;
        
    for (int i=0; i<weak.size(); i++) {
        int p = weak.front();
        weak.pop_front();
        int d = dist.back();
        dist.pop_back();

        vector<int> temp;
        int c = p+d;
        if(c > n)
            c %= n;
        while(!weak.empty()) {
            if(weak.front() <= c) {
                temp.push_back(weak.front());
                weak.pop_front();
            }
            else
                break;
        }
        func(n, weak, dist, deep+1);
        while(!temp.empty()) {
            weak.push_front(temp.back());
            temp.pop_back();
        }
        weak.push_back(p);
        dist.push_back(d);
    }
}
int solution(int n, vector<int> weak, vector<int> dist) {
    deque<int> temp;

    for(int i=0; i<weak.size(); i++)
        temp.push_back(weak[i]);

    func(n, temp, dist, 0);
    if(answer == 20)
        return -1;
    else
        return dist.size() - answer - 1;
}
```
재귀를 통해 모든 점에서 시작하는 경우의 수를 검사했다고 생각했는데 시간은 아슬아슬하게 통과한 것같지만 계산된 결과가 나의 생각과 다른 결과를 도출한 것 같다.  
4개의 케이스를 제외한 모든 테스트 케이스에서 실패했다.

*****

### 2차시도 (실패)
```cpp
int answer = 20;
void func(int n, deque<int> weak, vector<int> dist, int deep) {
    
    if (weak.empty()) {
        if (answer > deep)
            answer = deep;
        return;
    }
    if (dist.empty())
        return;
        
    for (int i=0; i<weak.size(); i++) {
        int p = weak.front();
        weak.pop_front();
        int d = dist.back();
        dist.pop_back();

        vector<int> temp;
        int c = p+d;
        while(!weak.empty()) {
            if (c < n) {
                if(p <= weak.front() && weak.front() <= c) {
                    temp.push_back(weak.front());
                    weak.pop_front();
                }
                else
                    break;
            }
            else {
                if(p <= weak.front() || weak.front() <= c%n) {
                        temp.push_back(weak.front());
                        weak.pop_front();
                }
                else
                    break;
            }
        }

        func(n, weak, dist, deep+1);
        while(!temp.empty()) {
            weak.push_front(temp.back());
            temp.pop_back();
        }
        weak.push_back(p);
        dist.push_back(d);
    }
}

int solution(int n, vector<int> weak, vector<int> dist) {
    deque<int> temp;

    for(int i=0; i<weak.size(); i++)
        temp.push_back(weak[i]);
    sort(dist.begin(), dist.end());
    func(n, temp, dist, 0);

    if(answer == 20)
        return -1;
    else
        return answer;
}
```
이전 코드에서 현재 인원이 점검할 수 있는 위치를 계산하는 과정에서 조건을 잘못 설정하여 많은 문제가 발생했음을 알아채고 조건을 정확하게 수정했다.  
하지만 그 과정에서 분기가 하나 추가되어서 그런지 이전에 발생하지 않았던 시간 초과가 발생한 케이스가 생겨버렸다.  
시간을 줄일수 있는 방법을 고민해봐야 할 것 같다.

*****

### 3차시도 (성공)
```cpp
int answer = 20;
void func(int n, deque<int> weak, vector<int> dist, int deep) {
    if (deep >= answer)
        return;
    if (weak.empty()) {
        answer = deep;
        return;
    }
    if (dist.empty())
        return;
        
    for (int i=0; i<weak.size(); i++) {
        int p = weak.front();
        weak.pop_front();
        int d = dist.back();
        dist.pop_back();

        vector<int> temp;
        int c = p+d;
        while(!weak.empty()) {
            if (c < n) {
                if(p <= weak.front() && weak.front() <= c) {
                    temp.push_back(weak.front());
                    weak.pop_front();
                }
                else
                    break;
            }
            else {
                if(p <= weak.front() || weak.front() <= c%n) {
                        temp.push_back(weak.front());
                        weak.pop_front();
                }
                else
                    break;
            }
        }

        func(n, weak, dist, deep+1);
        while(!temp.empty()) {
            weak.push_front(temp.back());
            temp.pop_back();
        }
        weak.push_back(p);
        dist.push_back(d);
    }
}

int solution(int n, vector<int> weak, vector<int> dist) {
    deque<int> temp;

    for(int i=0; i<weak.size(); i++)
        temp.push_back(weak[i]);
    sort(dist.begin(), dist.end());
    func(n, temp, dist, 0);

    if(answer == 20)
        return -1;
    else
        return answer;
}
```
이전 코드에서 이미 답보다 더 많은 인원이 투입되는 경우는 바로 다음 경우로 넘어가게 함으로써 시간을 줄였다.  
처음에는 재귀함수 시작부분에 조건문만 추가하여 풀어 보았으나 여전히 시간초과가 발생하여 고민 해본 결과 answer을 저장하는 부분에서 이미 이전에 더 많은 인원이 투입되는 경우를 계산했음으로 저장하는 부분에서는 상기 조건문이 필요없다는 것이 확인되어 삭제하고 돌려서 정말 아슬아슬하게 통과했다.