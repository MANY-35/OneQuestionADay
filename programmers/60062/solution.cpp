#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int func(int n, deque<int> weak, vector<int> dist) {
    
    if (weak.empty())
        return 1;
    if (dist.empty())
        return -1;


    int d = dist.back();
    dist.pop_back();
    for(int i=0; i<weak.size(); i++) {
        int w = weak.front();
        weak.pop_front();
        cout << w << " " << d << endl;
        deque<int> cash;
        cash.push_back(w);
        while (d+w >= weak.front() || (d+w)%n >= weak.front())
        {
            cash.push_front(weak.front());
            weak.pop_front();
        }

        cout << "number : ";
        for(int l=0; l<weak.size(); l++)
            cout << weak[l] << " ";
        cout << endl;

        cout << "cash : ";
        for (int l : cash) {
            cout << l << " ";
        }
        cout << endl;
        
        func(n, weak, dist);

        cout << "end func" << endl;
        for (int k : cash) {
            weak.push_back(k);
        }
        for (int l : weak) {
            cout << l << " ";
        }

        cout << endl;
    }
    return 1;
}

int solution(int n, vector<int> weak, vector<int> dist) {
    int answer = 0;

    deque<int> temp;

    for(int i=0; i<weak.size(); i++)
        temp.push_back(weak[i]);

    cout << func(n, temp, dist) << endl;

    return answer;
}

int main(void) {
    int n = 12;
    vector<int> weak = {
        1, 5, 6, 10
    };
    vector<int> dist = {
        1, 2, 3, 4
    };

    solution(n, weak, dist);

}