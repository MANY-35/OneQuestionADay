# LV3 스타 수열

### 1차시도 (실패)
```cpp
#include <string>
#include <vector>
#include <map>
using namespace std;

void permutation(vector<vector<int>> &per, vector<int> &arr, vector<int> t, int c, int n) {
    if(n-t.size() > arr.size()-c)
        return;
    if(t.size() == n) {
        per.push_back(t);
        return;
    }
    for(int i=c; i<arr.size(); i++) {
        t.push_back(arr[i]);
        permutation(per, arr, t, i+1, n);
        t.pop_back();
    }
}
bool checkStar(vector<int> &arr) {
    map<int, int> t;
    int max = 0;
    for(int i=0; i<arr.size(); i+=2) {
        if(arr[i] == arr[i+1])
            return false;
        for (int j=0; j<2; j++) {
            t[arr[i+j]]++;
            if(max < t[arr[i+j]])
                max = t[arr[i+j]];
        }
    }
    if (arr.size()/2 == max)
        return true;
    return false;
}
int solution(vector<int> a) {
    if (a.size() < 2)
        return 0;
    else if(a.size() == 2) {
        if(a[0] == a[1])
            return 0;
        else
            return 2;
    }

    int i = 2;
    while(i+2 <= a.size())
        i+=2;

    
    for(; i > 2; i-=2) {
        vector<vector<int>> p = {};
        permutation(p, a, {}, 0, i);
        for(auto k : p) {
            if (checkStar(k))
                return i;
        }
    }
    return 0;
}
```
> 순열을 만들고 주어진 스타배열의 조건에 맞는지 검사만하면 되는 간단한 문제였으나 작성한 코드에서 순열의 중복을 처리하지 못해 절반이 넘는 케이스에서 시간초과가 발생했다.
> 순열을 구하는 함수에서 중복을 확인하는 방법이 있는지 고민해봐야 할 것 같다.

*****

### 2차시도 (실패)
```cpp
void permutation(map<vector<int>, int> &per, vector<int> &arr, vector<int> t, int c, int n) {
    if(n-t.size() > arr.size()-c)
        return;
    if(t.size() == n) {
        per[t] = 0;
        return;
    }
    for(int i=c; i<arr.size(); i++) {
        t.push_back(arr[i]);
        permutation(per, arr, t, i+1, n);
        t.pop_back();
    }
}

bool checkStar(vector<int> arr) {
    map<int, int> t;
    int max = 0;
    for(int i=0; i<arr.size(); i+=2) {
        if(arr[i] == arr[i+1])
            return false;
        for (int j=0; j<2; j++) {
            t[arr[i+j]]++;
            if(max < t[arr[i+j]])
                max = t[arr[i+j]];
        }
    }
    if (arr.size()/2 == max)
        return true;
    return false;
}

int solution(vector<int> &a) {
    if (a.size() < 2)
        return 0;
    else if(a.size() == 2) {
        if(a[0] == a[1])
            return 0;
        else
            return 2;
    }

    int i = 2;
    while(i+2 <= a.size())
        i+=2;

    for(; i > 2; i-=2) {
        map<vector<int>, int> p = {};
        permutation(p, a, {}, 0, i);
        for(auto k : p) {
            if (checkStar(k.first))
                return i;
        }
    }
    return 0;
}
```
> map을 이용해 순열에서 중복을 제거 해봤는데 여전히 시간초과가 발생한다.
고민해보니 순열을 구하는것 자체가 문제가 있는 것 같다.

*****

### 2차시도 (실패)
```cpp
int solution(vector<int> a) {
    int len = a.size();
    if (len < 2)
        return 0;
    else if(len == 2) {
        if(a[0] == a[1])
            return 0;
        else
            return 2;
    }
    map<int, vector<int>> numbers;
    for(int i=0; i<len; i++)
        numbers[a[i]].push_back(i);

    int answer = 0;
    for(auto number : numbers) {
        number.second.push_back(len);
  
        int sum = 1;
        if(number.second[0] == 0)
            number.second[0] = 1;
        for(int i=1; i<number.second.size()-1; i++) {
            if(number.second[i] - number.second[i-1] - 1 > 0)
                sum++;
            else if(number.second[i+1] - number.second[i] - 1 > 0) {
                sum++;
                number.second[i]++;
            }   
        }
        if (answer < sum)
            answer = sum;
    }
    return answer*2;
}
```
> 처음 부터 스타 수열의 가능여부를 기준으로 주어진 수열을 판단하는 방향으로 진행 해보았다.
>각 숫자마다 위치를 부여한 후 위치에 따라 스타 수열을 만들 때 최대 길이를 구하는 방식으로 코드를 작성했다.
>하지만 3개의 케이스에서 실패했다. 어떤 예외가 있는지 고민해봐야 겠다. 

*****

### 3차시도 (성공)
```cpp
int solution(vector<int> a) {
    int len = a.size();
    if (len < 2)
        return 0;
    else if(len == 2) {
        if(a[0] == a[1])
            return 0;
        else
            return 2;
    }

    map<int, vector<int>> numbers;
    for(int i=0; i<len; i++)
        numbers[a[i]].push_back(i);
    
    if (numbers.size() < 2)
        return 0;
    
    int answer = 0;
    for(auto number : numbers) {
        number.second.push_back(len);
  
        int sum = 0;
        if(number.second[0] - 0 > 0)
            sum++;
        else if(number.second[1] - number.second[0] - 1 > 0) {
            sum++;
            number.second[0]++;
        }
        for(int i=1; i<number.second.size()-1; i++) {
            if(number.second[i] - number.second[i-1] - 1 > 0)
                sum++;
            else if(number.second[i+1] - number.second[i] - 1 > 0) {
                sum++;
                number.second[i]++;
            }   
        }
        if (answer < sum)
            answer = sum;

    }
    return answer*2;
}
```
>같은 숫자만 3개이상 존재하는 경우에 무조건 2가 출력되는 문제가 있는 것을 알아냈고, 이전 코드에서 숫자의 시작인덱스가 0인 경우 무조건 1을 증가시킨다음 구하는 방식에서 문제가 있다는 것을 알고 수정했다.
