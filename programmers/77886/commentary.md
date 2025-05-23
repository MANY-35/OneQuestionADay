# LV3 110 옮기기

### 1차시도 (실패)
```cpp
vector<string> solution(vector<string> s) {
    vector<string> answer;

        for (string str : s) {
        int left = 0, right = 0;
        while(left < str.size()-3) {
            int stack = 0;
            while (stack < 3 && left < str.size()) {
                if(str[left] == '1')
                    stack++;
                else 
                    stack = 0;
                left++;
            }

            if(stack < 3)
                break;

            left--;
            for (right = left-2; right<str.size(); right++) {
                if(str[right] == '0' && str[right-1] == '1' && str[right-2] == '1')
                    break;
            }
            str[left] = '0';
            str[right] = '1';
            left++;
        }
        
        answer.push_back(str);
    }

    return answer;
}
```
제일 처음에 만나는 111을 기준으로 그 다음으로 오는 110과 스위칭해주는 방식으로 코드를 작성해봤다.  
하지만 단 한개의 케이스만 통과했으며 두 개의 케이스는 시간 초과가 발생했고, 나머지는 모두 실패했다.  
>처음 주어지는 예제를 모두 통과해서 어느부분에서 문제인지 찾는데 상당한 시간이 걸렸으나 찾지못하여 검색을 해보니 처음 부분에서 110이 먼저 나오고 그뒤에 0이 바로 있는 경우 0이 당겨지면서 더 작은 값이 된다는 사실을 깨달았다.

*****

### 2차시도 (실패)
```cpp
vector<string> solution(vector<string> s) {
    vector<string> answer;
    for (string str : s) {
        vector<char> stack = {str[0]};
        int count = 0;
        char last = str[1];
        for(int i=2; i<str.size(); i++) {
            if(str[i] == '0' && last == '1' && stack.back() == '1') {
                count++;
                stack.pop_back();
                last = stack.back();
                stack.pop_back();
            }
            else {
                stack.push_back(last);
                last = str[i];
            }
        }
        stack.push_back(last);
        int i;
        for(i=stack.size()-1; i>=0; i--) {
            if (stack[i] == '0')
                break;
        }
        string left(stack.begin(), stack.begin()+i+1);
        string right(stack.begin()+i+1, stack.end());
        for(int j=0; j<count; j++)
            left += "110";
        left += right;
        answer.push_back(left);
    }
    return answer;
}
```
주어진 문자열에서 가능한 모든 110의 갯수를 구한뒤 제거해주고 남은 문자열에서 뒤에서부터 0을 만나는 시점에 모든 110을 더해주는 방식으로 수정했다.  
하지만 단 한개의 케이스에서 실패했다. 어떤 예외가 발생한건지 고민해봐야 할 것 같다.

*****

### 3차시도 (성공)
```cpp
vector<string> solution(vector<string> s) {
    vector<string> answer;
    for (string str : s) {
        vector<char> stack = {str[0]};
        int count = 0, s_i =0;
        for (int i=1; i<str.size(); i++) {
            if(s_i < 1) {
                stack.push_back(str[i]);
                s_i++;
            } else {
                if (stack[s_i-1] == '1' && stack[s_i] == '1' && str[i] == '0') {
                    count++;
                    stack.pop_back();
                    stack.pop_back();
                    s_i -= 2;
                } else {
                    stack.push_back(str[i]);
                    s_i++;
                }
            }
        }
        int index;
        for(index=stack.size()-1; index>=0; index--) {
            if (stack[index] == '0')
                break;
        }
        string left(stack.begin(), stack.begin()+index+1);
        string right(stack.begin()+index+1, stack.end());
        for(int j=0; j<count; j++)
            left += "110";
        left += right;
        answer.push_back(left);
    }
    return answer;
}
```
last = str[1] 이라는 한 글자로 이루어진 문자열을 고려하지 않았다.
> ~~작업하던 vscode에서 자연스럽게 출력이 되서 전혀 이상함을 못 느꼇다.~~
