#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(vector<vector<int>> board) {
    int n = board.size();
    vector<vector<int>> visted(n, vector<int>(n, 0));

    queue<vector<int>> que;
    que.push({0,0,0,1,0});

    


    return visted[n-1][n-1];

}

int main(void) {
    vector<vector<int>> board = {
        {0, 0, 0, 1, 1},
        {0, 0, 0, 1, 0},
        {0, 1, 0, 1, 1},
        {1, 1, 0, 0, 1},
        {0, 0, 0, 0, 0}
    };
    cout << solution(board) << endl;
}