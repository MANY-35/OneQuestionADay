#include <string>
#include <vector>
#include <queue>
using namespace std;


// vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
//     vector<int> answer;
//     vector<vector<int>> arr(n+1);
//     for (auto road : roads) {
//         arr[road[0]].push_back(road[1]);
//         arr[road[1]].push_back(road[0]);
//     }
    
//     for (int start : sources) {
//         queue<int> que;
//         que.push(start);
//         vector<bool> visit(n);
//         vector<int> dist(n);
//         visit[start] = true;
//         dist[start] = 0;

//         while(!que.empty()) {
//             int t = que.front();
//             que.pop();
//             if (t == destination) {
//                 answer.push_back(dist[t]);
//                 que.push(0);
//                 break;
//             }
//             for(int i : arr[t]) {
//                 if (visit[i])
//                     continue;
                
//                 que.push(i);
//                 visit[i] = true;
//                 dist[i] = dist[t] + 1;
//             }
//         }
//         if(que.empty()) {
//             answer.push_back(-1);
//         }
//     }
//     return answer;
// }

 vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer(n, -1);

    
    return answer;
 }

int main(void) {
    int n = 5;
    vector<vector<int>> roads = {
        {1, 2}, {1, 4}, {2, 4}, {2, 5}, {4, 5}
    };

    vector<int> sources = {
        1,3,5
    };
    int destination = 5;

    solution(n, roads, sources, destination);
}