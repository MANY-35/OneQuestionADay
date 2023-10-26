#include<iostream>
#include<vector>
#include <map>

using namespace std;


vector<int> solution(vector<string> enroll,  vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer(enroll.size());
    vector<int> referral_i(referral.size());

    for(int i=0; i<referral.size(); i++) {
        if (!referral[i].compare("-")) {
            referral_i[i] = 0;
        }
        else {
            referral_i[i] = 0;
            for(int j=0; j<enroll.size(); j++) {
                if (!enroll[j].compare(referral[i])) {
                    referral_i[i] = j+1;
                    break;
                }
            }
        }
    }

    for (int i=0; i<seller.size(); i++) {
        int target;
        for(int j=0; j<enroll.size(); j++) {
            if (!enroll[j].compare(seller[i])) {
                target = j+1;
                break;
            }
        }
        int cost = amount[i] * 100;
        while (target > 0) {
            if (cost * 0.1 <= 0) {
                answer[target-1] += cost;
                break;
            }
            else
                answer[target-1] += cost - int(cost * 0.1);
            cost = cost * 0.1;
            target = referral_i[target-1];
        }
    }

    return answer;
}

int main(void) {

    vector<string> enroll = {
        "john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"
    };
    vector<string> referral = {
        "-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"
    };
    vector<string> seller = {
        "young", "john", "tod", "emily", "mary"
    }; 
    vector<int> amount = {
        12, 4, 2, 5, 10
    };

    for(auto i : solution (enroll, referral, seller, amount)) {
        cout << i << " ";
    }
    cout << endl;
}