def answer():
    m = int(input())
    grid = [list(map(int, input().split())) for i in range(m)]
    dp = [[0 for i in range(3)] for j in range(m)]
    for i in range(3): dp[m-1][i] = grid[m-1][i]

    for i in range(m-2, -1, -1):
        for j in range(2, -1, -1):
            if j == 0:
                dp[i][j] = max(dp[i+1][1], dp[i+1][2]) + grid[i][j]
            elif j == 1:
                dp[i][j] = max(dp[i+1][0], dp[i+1][2]) + grid[i][j]
            else:
                dp[i][j] = max(dp[i+1][0], dp[i+1][1]) + grid[i][j]

    return max(dp[0])



print(answer())
