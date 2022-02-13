#왼쪽 위 (1, 1)에서 출발하여 오른쪽 아래 (n, m)에 도착해야 함
n, m = map(int, input().split())
#다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화 ((0, _), (_, 0)도 전부)
dp = [[0]*(m+1) for _ in range(n+1)]

#다이나믹
for x in range(1, n+1):
    for y in range(1, m+1):
        if x == 1 and y == 1:
            dp[x][y] = 1
        else:
            dp[x][y] = dp[x-1][y] + dp[x][y-1] + dp[x-1][y-1]

print(dp[n][m] % 1000000007)