#include<iostream>
#include<vector>
using namespace std;

int main(void) {
    int tc;
    vector<string> answer;
    
    cin >> tc;
    while (tc--) {
        string cmd;

        cin >> cmd;
        
        int len;
        cin >> len;

        string t;
        cin >> t;

        vector<string> arr;
        string temp = "";
        for(int i=1; i<t.length(); i++){
            if (t[i] != ',' && t[i]!=']')
                temp += t[i];
            else{
                arr.push_back(temp);
                temp = "";
            }
        }
        int re = 1;
        int s = 0;
        int e = len-1;

        for(char c : cmd){
            if (c == 'R') {
                re *= -1;
                int t = s;
                s = e;
                e = t;
            }
            else {
                len -= 1;
                s += re;
            }
            
            if (len < 0){
                break;
            }
 
        }
        if (len < 0){
            answer.push_back("error");
        }
        else if(len == 0){
            answer.push_back("[]");
        }
        else {
            string t= "[";
            for(int i=s; i!=e; i+=re){
                t += arr[i] + ",";
            }
            t += arr[e] + "]";
            answer.push_back(t);
        }
    }
    for (auto k : answer) {
        cout << k <<endl;
    }
    return 0;
}