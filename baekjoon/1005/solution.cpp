#include<iostream>
#include<vector>
#include<queue>
using namespace std;


struct cmp {
    bool operator()(vector<int> a, vector<int>b) {
        if (a[1] > b[1])
            return true;
        return false;
    }
};

int main(void) {
    int TC;
    cin >> TC;
    vector<int> answer;
    while (TC--) {
        int N, K; // 건물 , 규칙
        cin >> N >> K;
        
        int *timecost = new int[N];
        for(int i=0; i<N; i++)
            cin >> timecost[i];

        int *code = new int[N];
        int s = 1;
        for (int i=0; i<N; i++, s*= 2)
            code[i] = s;

        int *possable = new int[N]();
        for(int i=0; i<K; i++) {
            int x, y;
            cin >> x >> y;
            possable[y-1] += code[x-1];
        }
        int vic;
        cin >> vic;

        int building = 0;
        int time = 0;
        priority_queue<vector<int>, vector<vector<int>>, cmp> que;
        while (building < s/2) {
            for(int i=0; i<N; i++) {
                if (possable[i] < 0)
                    continue;
                int p = building&possable[i];
                if (p == possable[i]) {
                    possable[i] = -1;
                    que.push(vector<int> {i, time+timecost[i]});
                }
            }
            time = que.top()[1];
            building += code[que.top()[0]];
            cout << time << " " << building << endl;
            if (que.top()[0] == vic)
                break;
            
            que.pop();
        }

        cout << (time);
    }
}