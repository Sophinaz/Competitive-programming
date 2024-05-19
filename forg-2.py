n, k= map(int, input().split())
nums = list(map(int, input().split()))
dp = [float('inf')] * n
dp[-1] = 0

for i in range(n-2, -1, -1):
    ans = float('inf')
    for j in range(1, k+1):
        if i+j < n: 
            ans = min(ans, abs(nums[i] - nums[i+j]) + dp[i+j])
    
    dp[i] = ans

print(dp[0])
