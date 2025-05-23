# LV3 표현 가능한 이진트리

### 1차시도 (성공)
```cpp
int checking(string str, int len) {
    if(len == 1)
        return str[0] - '0';
    else {
        string left = "";
        for(int i=0; i<len/2; i++)
            left += str[i];
        
        string right = "";
        for(int i=len/2+1; i<len; i++)
            right += str[i];

        int l = checking(left, len/2);
        if(l == -1)
            return -1;
        int r = checking(right, len/2);
        if (r == -1)
            return -1;
            
        if(str[len/2]=='0') {
            if(r+l > 0)
                return -1;
            else
                return 0;
        }
        else
            return 1;
    }
}
vector<int> solution(vector<long long> numbers) {
    vector<int> answer;

    for(auto number : numbers) {
        string binStr = "";
        
        while(number) {
            if (number%2)
                binStr = "1" + binStr;
            else
                binStr = "0" + binStr;
            number /= 2;
        }
        
        int binlen = binStr.size();
        int sum = 0;
        for(int bit=1; sum < binlen; bit*=2)
            sum += bit;

        string str = "";
        for(int i=binlen; i<sum; i++)
            str += "0";
        str += binStr;

        if(checking(str, sum) == 1)
            answer.push_back(1);
        else
            answer.push_back(0);
    }

    return answer;
}
```
문제를 받고 트리를 어떻게 구성할 수 있는지 살펴보았는데  
정이진트리를 기본으로 하기 때문에 받은 숫자의 이진수를 뒤에서부터 구성하면 될 것 같다는 느낌을 받았고,  
주어진 숫자를 정이진트리로 바꾸기 위해서는 노드의 갯수를 구하는 것부터 시작해야겠다고 생각했다.  
노드의 갯수를 구한뒤 주어진 수를 이진수로 바꾸고 나머지 부분을 0으로 채워 넣어서 생긴 문자열을 가지고 고민해본 결과 가장 가운데 있는 노드가 항상 루트 노드인 것을 떠올렸다.  
루트 노드를 기준으로 좌측 서브트리와 우측 서브트리를 나누어 가면서 경의 수를 생각해봤다.  
루트노드가 0이 될 수 있는 경우는 트리 전체가 모드 0인 경우 밖에 없었다.  
그 경우를 생각하면서 코드를 작성했다.

> ~~사실 첫 채점은 0점이 나왔다다~~   
하나를 실패하고 나머지는 에러가 발생해서 한참 헤맸다.   
다시 천천히 생각해보니 처음 노드의 수를 결정하는 부분에서 문제가 있다는 것을 알고 수정했다.  
또한 문자를 숫자 1과 0으로 변환하는 과정에서 ASCII코드를 생각하지 않고 풀어서 틀렸다는 사실을 깨달았다.  
>시간을 더욱 줄이기 위해서 함수에 문자열의 길이를 주는것이아니라 시작점과 끝점을 주어서 문자열 복사없이 수행하도록 하는것이 좋아보인다.