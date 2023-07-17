#include <iostream>
#include <vector>
// #include <utility>
using namespace std;

int main(void) {
    int M, N;
    vector<vector<int>> v;

    cin >> M >> N;

    v.push_back(vector<int>(M+2, -1));
    for(int i=0; i<N; i++) {
        vector<int> temp;
        int input;
        temp.push_back(-1);
        for(int j=0; j<M; j++) {
            cin >> input;
            temp.push_back(input);
        }
        temp.push_back(-1);
        v.push_back(temp);
    }
    v.push_back(vector<int>(M+2, -1));

    vector<pair<int, int>> check;
    for(int i=1; i<N+1; i++) {
        for(int j=1; j<M+1; j++) {
            if (v[i][j] == -1)
                continue;

            if(v[i-1][j] == -1 && v[i][j-1] == -1 && v[i+1][j] == -1 && v[i][j+1] == -1) {
                if(v[i][j] == 0){
                    cout << -1;
                    return 0;
                }
            }
            else if(v[i][j] == 1){
                check.push_back(pair<int, int>(i,j));
            }
        }
    }
    int answer = -1;
    do{
        vector<pair<int, int>> sub;
        for(auto k : check) {
            pair<int, int> t = k;
            if (v[t.first][t.second+1] == 0) {
                sub.push_back(pair<int, int>(t.first, t.second+1));
                v[t.first][t.second+1] = 1;
            }
            if (v[t.first][t.second-1] == 0) {
                sub.push_back(pair<int, int>(t.first, t.second-1));
                v[t.first][t.second-1] = 1;
            }
            if (v[t.first+1][t.second] == 0) {
                sub.push_back(pair<int, int>(t.first+1, t.second));
                v[t.first+1][t.second] = 1;
            }
            if (v[t.first-1][t.second] == 0) {
                sub.push_back(pair<int, int>(t.first-1, t.second));
                v[t.first-1][t.second] = 1;
            }
        }
        check = sub;
        answer ++;
    }while(!check.empty());

    for(int i=1; i<N+1; i++) {
        for(int j=1; j<M+1; j++)
        {
            if(v[i][j]==0)
            {
                cout << -1;
                return 0;
            }
        }
    }
    cout << answer << endl;
    return 0;
}