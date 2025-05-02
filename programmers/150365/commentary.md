# LV3 미로 탈출 명령어

### 1차시도 (실패)
```cpp
int abs(int a) {
    if (a > 0)
        return a;
    return -a;
}
string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";
    int ud = 0, lr = 0;
    ud = r - x;
    lr = c - y;
    int sum = abs(ud) + abs(lr);
    if (sum > k || (k-sum)%2 != 0)
        return "impossible";

    while (x < r) {
        answer += "d";
        x++;
        k--;
    }
    while (y > c) {
        answer += "l";
        y--;
        k--;
    }
    while (y < c) {
        answer += "r";
        y++;
        k--;
    }
    while (x > r) {
        answer += "u";
        x--;
        k--;
    }
    if (k == 0)
        return answer;
    bool rr, ll, uu, dd;
    rr = ll = uu = dd = false;
    if (x < n)
        dd = true;
    if (x > 1)
        uu = true;
    if (y < m)
        rr = true;
    if (y > 1)
        ll = true;
    while(k >= 4) {
        if(dd) {
            if (ll)
                answer += "dlru";
            else if(rr)
                answer += "drul";
            else
                answer += "dudu";
        }
        else if(ll)
            answer += "lrlr";
        else if(rr)  
            answer += "rlrl";
        k-=4;
    }
    if (k > 0) {
        if(dd)
            answer += "du";
        else if(ll)
            answer += "lr";
        else if(rr)
            answer += "rl";
        else 
            answer += "ud";
    }
    return answer;
}
```
이동횟수가 주어지기 때문에 이동횟수를 가지고 탈출할 수 있는지 먼저 판단할 수 있다.  
그후 미로를 탈출할 때 주어진 우선순위가 존재하기 때문에 순서대로 탈출구까지 이동 시킨 후 그다음 남은 이동횟수를 소진시키면 된다고 생각했다.  
그 과정에서 경우의 수를 생각하여 이동을 시켰다고 생각했는데 3개의 케이스말고는 전부 오답이였다.  
아무래도 불가능한 경우만 정답처리 된 것으로 보인다.
> 다시 생각해보니 지금같은 코드에선 목적지에서 아래 2칸과 왼쪽2칸이 비어있어도 dlru 순으로 움직이는데 dduu 가 맞는 움직임이다.

*****

### 2차시도 (성공)
```cpp
int dis(int x, int y, int r, int c) {
    return ((c > y) ? c-y : y-c) + ((r > x) ? r-x : x-r);
}
string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";
    int sum = dis(x, y, r, c);
    
    cout << sum << endl;

    if (sum > k || (k-sum)%2 != 0)
        return "impossible";
    

    while(x < n && k >= dis(x,y,r,c)) {
        answer += "d";
        k--;
        x++;
    }
    while(k >= dis(x,y,r,c) && k > 0) {
        if(y > 1) {
            answer += "l";
            y--;
        }
        else { 
            answer += "r";
            y++;
        }
        k--;
    }

    while (x < r) {
        answer += "d";
        x++;
    }
    while (y > c) {
        answer += "l";
        y--;
    }
    while (y < c) {
        answer += "r";
        y++;
    }
    while (x > r) {
        answer += "u";
        x--;
    }

    return answer;
}
```
이전코드에서 현재 위치에서 탈출 지점까지의 거리와 이동 가능한 횟수를 바탕으로 아래로 내려갈 수 있는 만큼 내려간 후 마찬가지로 다른 방향으로도 움직여주면 되는 문제였다. 
>풀고나서 다른 사람의 풀이를 보니 내 코드가 조금 더럽다고 느껴졋다. 나는 움직이는 만큼 미리 다 움직이고 탈출지점 까지 움직이는 방식으로 풀었는데 처음부터 조건문을 통해 거리와 횟수를 바탕으로 하나의 반복문으로 해결할 수 있었다.
