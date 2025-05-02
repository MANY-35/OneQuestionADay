# LV2 이모티콘 할인

### 1차시도 (실패)
```py
import itertools
def solution(users, emoticons):
    # 할인율을 소수로 표현 (0.9 = 10% 할인)
    discounts = [0.9, 0.8, 0.7, 0.6]
    discounted_prices = []
    for emoticon in emoticons:
        discounted_prices.append([])
        for dis in discounts:
            discounted_prices[-1].append(int(emoticon * dis))

    # 모든 가능한 할인 조합 생성
    discount_combinations = list(itertools.product([0,1,2,3], repeat=len(discounted_prices)))
    max_result = [0, 0]  # [플러스 서비스 가입자 수, 판매액]
    
    for indices in discount_combinations:
        # 현재 할인 조합에 대한 가격과 할인율 계산
        prices = [discounted_prices[i][indices[i]] for i in range(len(discounted_prices))]
        discount_rates = [i+1 for i in indices]  # 1~4 (10%~40% 할인)

        plus_users = total_sales = 0
        for user in users:
            user_spent = 0
            for i in range(len(prices)):
                if user[0]/10 <= discount_rates[i]:
                    user_spent += prices[i]
            if user_spent >= user[1]:
                plus_users += 1
                user_spent = 0
            total_sales += user_spent
            
        # 최대값 업데이트
        if max_result[0] < plus_users:
            max_result = [plus_users, total_sales]
        elif max_result[0] == plus_users and max_result[1] <= total_sales:
            max_result = [plus_users, total_sales]
    return max_result
```
3개의 데이터 케이스에서 실패했다.  
부동소수점 연산으로 인한 오류가 발생했다.

*****

### 2차시도 (성공)
```py
import itertools
def solution(users, emoticons):
    # 할인율을 정수로 표현 (90 = 10% 할인)
    discounts = [90, 80, 70, 60]
    discounted_prices = []
    for emoticon in emoticons:
        discounted_prices.append([])
        for dis in discounts:
            # 정수 나눗셈을 사용하여 부동소수점 오류 방지
            discounted_prices[-1].append((emoticon * dis)//100)

    max_result = [0, 0]  # [플러스 서비스 가입자 수, 판매액]
    for indices in itertools.product([0,1,2,3], repeat=len(discounted_prices)):
        # 현재 할인 조합에 대한 가격과 할인율 계산
        prices = [discounted_prices[i][indices[i]] for i in range(len(discounted_prices))]
        discount_rates = [i+1 for i in indices]  # 1~4 (10%~40% 할인)

        plus_users = total_sales = 0
        for user in users:
            user_spent = 0
            for i in range(len(prices)):
                if user[0]/10 <= discount_rates[i]:
                    user_spent += prices[i]
            if user_spent >= user[1]:
                plus_users += 1
                user_spent = 0
            total_sales += user_spent
            
        # 최대값 업데이트
        if max_result[0] < plus_users:
            max_result = [plus_users, total_sales]
        elif max_result[0] == plus_users and max_result[1] <= total_sales:
            max_result = [plus_users, total_sales]
    return max_result
```
> 부동소수점 연산 대신 정수 연산을 사용하여 문제를 해결했다.