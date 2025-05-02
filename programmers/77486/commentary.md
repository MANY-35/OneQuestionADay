# LV3 다단계 칫솔 판매

### 1차 시도 (성공)
```cpp
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
```
처음에는 map을 이용하여 모든 데이터를 트리형식으로 구현하는 것이 방법이라고 생각했으나 좀더 생각해보니 모든데이터가 연결되어있을 필요없이 각 노드의 다음 목적지만 알면 풀 수 있을것 같다는 생각을했다.  
그래서 목적지가 저장되어있는 referral 벡터를 응용하여 referral_i 벡터를 생성하여 다음 index의 정보를 저장하여 index가 0이 될때, 즉 루트노드에 도착할 때 까지 반복시키면서 cost를 계산하는 방식으로 코드를 작성하였다.  
중간에 10%의 이자가 0 이하가 되는 경우에 대한 조건을 처리하지 못해 다소 막히는 점이 있었지만 조건문을 이용하여 해결할 수 있었다.  
다만 몇개의 테스트 케이스에서 너무 오랜 시간이 걸리는데 반복을 줄 일수 있는 방법에 대해 고민해 보는 것도 좋을 것 같다.
>찾아보니 문자열 compare 메서드를 많이 사용하여 너무 많은 시간이 투자되는 것 같다.
