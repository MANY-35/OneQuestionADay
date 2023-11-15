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
        int count = 0, s_i =0;
        for (int i=1; i<str.size(); i++) {
            if(s_i < 1)
                stack.push_back(str[i]);
            else {
            
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
        cout << left;
    }

    return answer;
}

int main(void)
{
    vector<string> s = {"1110"};
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