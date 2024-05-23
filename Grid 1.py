m, n = map(int, input().split())
grid = [list(input()) for i in range(m)]
dp = [[0 for i in range(n)] for j in range(m)]
val = (10**9) + 7
def valid(r, c): return 0 <= r < m and 0 <= c < n and grid[r][c] == '.'

dp[-1][-1] = 1
for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        if valid(i, j+1): 
            dp[i][j] += dp[i][j+1]
        if valid(i+1, j): 
            dp[i][j] += dp[i+1][j]
print(dp[0][0]%val)
