text1 = input()
text2 = input()
result = ""

dp = [[0 for i in range(len(text1))] for i in range(len(text2))]
def valid(r, c):
    return 0 <= r < len(text2) and 0 <= c < len(text1)
for i in range(len(text2)):
    for j in range(len(text1)):
        if text1[j] == text2[i]:
            if valid(i-1, j-1):
                dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = 1
        else:
            x, y = -1, -1
            if valid(i, j-1): x = dp[i][j-1]
            if valid(i-1, j): y = dp[i-1][j]
            res = max(x, y)
            if res != -1: dp[i][j] = res
            else: dp[i][j] = 0

row, col = len(text2)-1, len(text1)-1
while len(result) != dp[-1][-1]:
    if text2[row] == text1[col]:
        result += text2[row]
        row -= 1
        col -= 1
    else:
        x, y = -1, -1
        if valid(row-1, col): x = dp[row-1][col]
        if valid(row, col-1): y = dp[row][col-1]
        
        if x > y: row -= 1
        else: col -= 1

print(result[::-1]) 
