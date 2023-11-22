#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

int solution(vector<int> a) {
    int len = a.size();
    if (len < 2)
        return 0;
    else if(len == 2) {
        if(a[0] == a[1])
            return 0;
        else
            return 2;
    }
    map<int, vector<int>> numbers;
    for(int i=0; i<len; i++)
        numbers[a[i]].push_back(i);

    if (numbers.size() < 2)
        return 0;

    int answer = 0;
    for(auto number : numbers) {
        number.second.push_back(len);

        cout << number.first << endl;
        for(int i=0; i<number.second.size(); i++) 
            cout << number.second[i] << " ";
        cout << endl;
        
        int sum = 0;
        if(number.second[0] - 0 > 0)
            sum++;
        else if(number.second[1] - number.second[0] - 1 > 0) {
            sum++;
            number.second[0]++;
        }
        for(int i=1; i<number.second.size()-1; i++) {
            if(number.second[i] - number.second[i-1] - 1 > 0)
                sum++;
            else if(number.second[i+1] - number.second[i] - 1 > 0) {
                sum++;
                number.second[i]++;
            }   
        }
        for(int i=0; i<number.second.size(); i++) 
            cout << number.second[i] << " ";
        if (answer < sum)
            answer = sum;
        cout << sum << endl;
        cout << endl;
    }

    return answer*2;
}

int main(void) {
    vector<int> a = {5, 5, 5, 6};
    cout << solution(a) << endl;
    
}   