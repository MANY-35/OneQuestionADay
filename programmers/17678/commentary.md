# LV3 [1차] 셔틀버스

### 1차 시도 (실패)
```cpp
string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    int time = 9 * 60;

    deque<int> timetable_int;
    sort(timetable.begin(), timetable.end());
    for (int i=0; i<=n*m && i < timetable.size(); i++) {
        int temp = 0;
        for (int j=4, c=1; j>=0; j--, c*=10) {
            if(j == 2) {
                c = 6;
                continue;
            }
            temp += ((timetable[i])[j]-'0') * c;
        }
        if (temp < time + n*t)
            timetable_int.push_back(temp);
    }
    for(int i=0; i<n-1; i++) {
        for (int j=0; j<m; j++) {
            if (timetable_int[0] > time)
                break;
            timetable_int.pop_front();
        }
        time += t;
    }

    if (timetable_int.size() >= m) 
        time = timetable_int[m-1] - 1;
    
    for (int i=0, k=600; i<4; i++, k/=10) {
        if(i == 2){
            k = 10;
            answer += ':';
        }
        answer += (time/k) + '0';
        time %= k;
    }
    return answer;
}
```
> 모든 데이터를 초로 치환하여 계산하도록 했고 정렬을 진행했으며 큐를 이용하여 데이터를 저장했다. 저장할 때 최대 운반 인원(셔틀버스의 운행 횟수 × 한 번에 이동 가능한 크루 수)만큼만 저장하도록 했다. 그 후 마지막 운행 전까지 이동 가능한 인원들을 큐에서 제거했고, 마지막 운행에서 대기하고 있는 인원이 셔틀에 탈 수 있는 인원보다 많다면 탈 수 있는 마지막 크루보다 1초 먼저 대기하도록 하고, 대기 인원이 셔틀에 수용 가능한 인원보다 적다면 마지막 운행 시간에 대기할 수 있도록 했다. 두 개의 테스트 케이스에서 실패했다. 하나의 케이스에서는 segmentation fault 에러가 발생한 것으로 보아 중간에 timetable_int[0] > time을 비교하는 과정에서 timetable_int가 반복 중에 비어있는 경우를 체크하지 않아 생긴 것으로 판단된다.

*****

# 2차 시도 (성공)
```cpp
string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    int time = 9 * 60;

    deque<int> timetable_int;
    sort(timetable.begin(), timetable.end());
    for (int i=0; i<=n*m && i < timetable.size(); i++) {
        int temp = 0;
        for (int j=4, c=1; j>=0; j--, c*=10) {
            if(j == 2) {
                c = 6;
                continue;
            }
            temp += ((timetable[i])[j]-'0') * c;
        }
        if (temp < time + n*t)
            timetable_int.push_back(temp);
    }
    for(int i=0; i<n-1; i++) {
        for (int j=0; j<m; j++) {
            if (timetable_int[0] > time)
                break;
            if (!timetable_int.empty())
                timetable_int.pop_front();
        }
        time += t;
    }

    if (timetable_int.size() >= m) 
        time = timetable_int[m-1] - 1;

    for (int i=0, k=600; i<4; i++, k/=10) {
        if(i == 2){
            k = 10;
            answer += ':';
        }
        answer += (time/k) + '0';
        time %= k;
    }
    return answer;
}
```
> 이전 실패했던 두 케이스 모두 timetable_int.pop_front()를 하는 과정에서 비어있는 메모리를 참조하는 케이스에서 발생한 문제였다.