#include <string>
#include <vector>
#include <iostream>
using namespace std;


int solution(vector<vector<int>> scores) {
    int answer = 1;
    vector<int> arr;

    arr.push_back(0);
    for (int i=1, sum=scores[0][0] + scores[0][1]; i<scores.size(); ++i) {
        if (sum < scores[i][0] + scores[i][1])
        {
            arr.push_back(i);
            answer ++;
        }
    }

    for (int i=0; i<arr.size(); ++i) {
         for (int j=1; j<arr.size(); ++j) {
            if(scores[arr[i]][0] < scores[arr[j]][0] && scores[arr[i]][1] < scores[arr[j]][1]) {
                answer --;
                if(i==0)
                    return -1;
                break;
            }
        }
    }

    return answer;
}

int main(void) {
    vector<vector<int>> scores =
    {
        {4,0},{2,5},{5,3},{2,6}
    };

    cout << solution(scores) << endl;
}