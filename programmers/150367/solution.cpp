#include <string>
#include <vector>
#include <iostream>

using namespace std;


int checking(string str, int len) {
    
    if(len == 1)
        return str[0] - '0';
    
    else {
        cout << "len = " << len << endl;
        string left = "";
        for(int i=0; i<len/2; i++)
            left += str[i];
        
        string right = "";
        for(int i=(len/2)+1; i<len; i++)
            right += str[i];
        
        cout << left << " in left" << endl;
        int l = checking(left, len/2);
        cout << l << " ";
        if(l < 0)
            return -1;
         
        cout << right << " in right" << endl;
        int r = checking(right, len/2);
        if(r < 0)
            return -1;


        if(str[len/2]=='0') {
            if(r + l > 0)
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
        {
            sum += bit;
            cout << sum << " ";
        }
        cout << endl;
        
        cout << binlen << " " << sum << endl;
        string str = "";
        for(int i=binlen; i<sum; i++)
            str += "0";
        str += binStr;
        cout << str << endl;

        if(checking(str, sum) == 1)
            answer.push_back(1);
        else
            answer.push_back(0);

        cout << answer.back() << endl;
    }

    return answer;
}

int main(void) {
    solution({2147516555});
}