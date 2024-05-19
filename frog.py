n = int(input())
nums = list(map(int, input().split()))
dp = [float('inf')] * n
dp[-1] = 0

for i in range(n-2, -1, -1):
    x = float('inf')
    if i < n-2: x = abs(nums[i] - nums[i+2]) + dp[i+2]
    y = abs(nums[i] - nums[i+1]) + dp[i+1]
    
    dp[i] = min(x, y)

print(dp[0])
