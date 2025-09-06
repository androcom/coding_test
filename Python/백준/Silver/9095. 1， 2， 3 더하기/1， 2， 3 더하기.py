def main():
    dp = [0] * 11
    # 초기값 설정
    dp[1] = 1  # 1
    dp[2] = 2  # 1+1, 2
    dp[3] = 4  # 1+1+1, 1+2, 2+1, 3

    """
    i = 4
    # 1 +3
    # 1+1 +2, 2 +2
    # 1+1+1 +1, 1+2 +1, 2+1 +1, 3 +1
    """
    for i in range(4,11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    N = int(input())
    for _ in range(N):
        n = int(input())
        print(dp[n])
        
main()