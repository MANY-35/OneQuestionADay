#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

void func(vector<vector<int>> &board, deque<vector<int>> que, int n) {

    deque<vector<int>> temp;
    while(!que.empty()) {
        vector<int> fr = que.front();

        que.pop_front();
        int head_y = fr[0]; int head_x = fr[1]; int tail_y = fr[2]; int tail_x = fr[3];
        cout << head_y << ", " << head_x << "| " << tail_y << ", " << tail_x << endl; 
        board[head_y][head_x] = fr[4];
        if (head_y == tail_y) {
            if(head_x+1 < n) {
                if(!board[head_y][head_x+1])
                    temp.push_back({head_y, head_x+1, head_y, head_x, fr[4]+1});
            }
            if(tail_x-1 > 0) {
                if(!board[tail_y][tail_x-1])
                    temp.push_back({tail_y, tail_x-1, tail_y, tail_x, fr[4]+1});
            }
            if(head_y+1 < n) {
                if(board[head_y+1][head_x]!=1 && board[tail_y+1][tail_x]!=1) {
                    if(!board[head_y+1][head_x]) {
                        temp.push_back({head_y+1, head_x, head_y, head_x, fr[4]+1});
                    }
                    if(board[tail_y+1][tail_x]==0) {
                        temp.push_back({tail_y+1, tail_x, tail_y, tail_x, fr[4]+1});
                    }
                }
            }
            if(head_y-1 > 0) {
                if(board[head_y-1][head_x]!=1 && board[tail_y+1][tail_x]!=1) {
                    if(!board[head_y-1][head_x]) {
                        temp.push_back({head_y-1, head_x, head_y, head_x, fr[4]+1});
                    }
                    if(!board[tail_y-1][tail_x]) {
                        temp.push_back({tail_y-1, tail_x, tail_y, tail_x, fr[4]+1});
                    }
                }
            }
        } 
        else {
            if(head_y+1 < n) {
                if(!board[head_y+1][head_x])
                temp.push_back({head_y+1, head_x, head_y, head_x, fr[4]+1});
            }
            if(tail_y-1 > 0) {
                if(!board[tail_y-1][tail_x])
                temp.push_back({tail_y-1, tail_x, tail_y, tail_x, fr[4]+1});
            }
            if(head_x+1 < n) {
                if(board[head_y][head_x+1]!=1 && board[tail_y][tail_x+1]!=1) {
                    if(!board[head_y][head_x+1]) {
                        temp.push_back({head_y, head_x+1, head_y, head_x, fr[4]+1});
                    }
                    if(!board[tail_y][tail_x+1]) {
                        temp.push_back({tail_y, tail_x+1, tail_y, tail_x, fr[4]+1});
                    }
                }
            }

            if(head_x-1 > 0) {
                if(board[head_y][head_x-1]!=1 && board[tail_y][tail_x-1]!=1) {
                    if(!board[head_y][head_x-1]) {
                        temp.push_back({head_y, head_x-1, head_y, head_x, fr[4]+1});
                    }
                    if(!board[tail_y][tail_x-1]) {
                        temp.push_back({tail_y, tail_x-1, tail_y, tail_x, fr[4]+1});
                    }
                }
            }
        }
    }

    for(auto k : temp) 
        cout << "{" << k[0] <<", " << k[1] << "} ";
    cout << endl;

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++)
            cout << board[i][j] << " ";
        cout << endl;
    }
    cout << endl;


    func(board, temp, n);
}


int solution(vector<vector<int>> board) {
    deque<vector<int>> que;
    board[0][0] = 2;
    board[0][1] = 2;
    que.push_back({0,1,0,0,2});

    func(board, que, board.size());
    return 0;
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