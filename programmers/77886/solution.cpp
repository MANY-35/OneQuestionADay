#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

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

        cout << left << endl;
    }

    return answer;
}

int main(void)
{
    vector<string> s = {"0100110"};
    // srand(time(NULL));
    // string str = "";
    // int k = rand();
    // for(int i=0; i<k%20; i++)
    // {   
    //     int n = rand();
    //     if(n%2)
    //         str+= "1";
    //     else 
    //         str+= "0";
    // }
    // cout << str << endl;
    // s.push_back(str);

    solution(s);
}