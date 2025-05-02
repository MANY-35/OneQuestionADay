# LV3 블록이동하기

### 1차시도 (실패)
```cpp
#include <string>
#include <vector>
#include <iostream>

using namespace std;
static int n;
void func(vector<vector<int>> &board, vector<vector<int>> &visted, int lx, int ly, int rx, int ry, int k) {
    if(k > visted[ry][rx] && visted[ry][rx])
        return;
    
    visted[ry][rx] = k;
    if(rx < n-1) {
        if(!board[ry][rx+1]){
            if(ly == ry)
                func(board, visted, rx, ry, rx+1, ry, k+1);
            else {
                if(!board[ly][lx+1])
                    func(board, visted, rx, ry, rx+1, ry, k+1);
            }
        }
    }
    if(ry < n-1) {
        if(!board[ry+1][rx]) {
            if(lx == rx)
                func(board, visted, rx, ry, rx, ry+1, k+1);
            else {
                if(!board[ly+1][lx])
                    func(board, visted, rx, ry, rx, ry+1, k+1);
            }
        }
    }
    if(rx > 0) {
        if(!board[ry][rx-1]) {
            if(ly == ry)
                func(board, visted, rx, ry, rx-1, ry, k+1);
            else {
                if(!board[ly][lx-1])
                    func(board, visted, rx, ry, rx-1, ry, k+1);
            }
        }
    }
    if(ry > 0) {
        if(!board[ry-1][rx]) {
            if(lx == rx)
                func(board, visted, rx, ry, rx, ry-1, k+1);
            else {
                if(!board[ly-1][lx])
                    func(board, visted, rx, ry, rx, ry-1, k+1);
            }
        }
    }
}
int solution(vector<vector<int>> board) {
    n = board.size();
    vector<vector<int>> visted(n, vector<int>(n, 0));
    visted[0][0] = 1;
    visted[0][1] = 1;
    visted[1][0] = 1;

    func(board, visted, 1, 0, 2, 0, 1);
    func(board, visted, 0, 0, 0, 1, 1);

    return visted[n-1][n-1];
}
```
단순히 생각해서 머리와 꼬리로 생각하고 풀었는데 당연하게도 한개의 케이스를 제외하고 전부 실패했다.  
그냥 풀다보니 dfs느낌으로 진행하게 되었는데 움직이는 방향에 머리를 정한것 부터 잘못됐다.  
주어진 문제에서는 양방향에서 모두 움직일 수 있다는 조건이 있엇고, 풀다보니 bfs방식으로 접근해야 할 것 같은 기분이 들었다.