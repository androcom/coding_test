def main():    
    N = int(input())

    if N == 1:
        print(0)
        return

    else:
        dp = [0] * (N + 1)  # index와 N 범위 일치
        """
        1을 빼는 연산은 항상 가능
        나눗셈과 뺄셈을 한 경우를 비교하여 더 작은 값 선택
        """
        for i in range(2, N + 1):
            # 1을 빼는 경우
            dp[i] = dp[i - 1] + 1
            
            # 2로 나누어 떨어지는 경우
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)
            
            # 3으로 나누어 떨어지는 경우
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i // 3] + 1)
                
        print(dp[N])

main()