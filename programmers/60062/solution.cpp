#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int answer = 20;
void func(int n, deque<int> weak, vector<int> dist, int deep) {
    if (deep >= answer)
        return;
    if (dist.empty())
        return;

    if (weak.empty()) {
        answer = deep;
        cout << "deep = " << deep << " answer = " << answer << endl;
        return;
    }
    
        
    for (int i=0; i<weak.size(); i++) {
        int p = weak.front();
        weak.pop_front();
        int d = dist.back();
        dist.pop_back();
    
        cout << d << " : (" << p << " ~ "<< p+d << ") = [" << p << " ";

        vector<int> temp;
        int c = p+d;
        
        while(!weak.empty()) {
            if (c < n) {
                if(p <= weak.front() && weak.front() <= c) {
                    cout << weak.front() << " ";
                    temp.push_back(weak.front());
                    weak.pop_front();
                }
                else
                    break;
            }
            else {
                if(p <= weak.front() || weak.front() <= c%n) {
                    cout << weak.front() << " ";
                    temp.push_back(weak.front());
                    weak.pop_front();
                }
                else
                    break;
            }
        }
        cout << "]" << endl << "in que : ";
        for(int k : weak) {
            cout << k << " ";
        }
        cout << endl;

        func(n, weak, dist, deep+1);
        while(!temp.empty()) {
            weak.push_front(temp.back());
            temp.pop_back();
        }
        weak.push_back(p);
        dist.push_back(d);
        cout << endl;
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

int main(void) {
    int n = 200;
    vector<int> weak = {
        0, 10, 50, 80, 120, 160
    };
    vector<int> dist = {
        1, 10, 5, 40, 30
    };

    cout << solution(n, weak, dist) << endl;

}