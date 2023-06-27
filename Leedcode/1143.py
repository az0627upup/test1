def solution(lis1, lis2):
    m, n = len(lis1), len(lis2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if lis1[i-1] == lis2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


def solutioning(lis1, lis2):
    m, n = len(lis1), len(lis2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_len = 0
    row, col = 0, 0
    str = ""
    for i in range(1, m+1):
        for j in range(1, n+1):
            if lis1[i-1] == lis2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    row = i
                    col = j
    k = dp[row][col]
    while k > 0:
        str += (lis1[row-1])
        row -= 1
        k -= 1
    lstr = str[::-1]
    return max_len, lstr


if __name__ == '__main__':
    x1 = input()
    x2 = input()
    # fc = solution(x1, x2)
    len, fc = solutioning(x1, x2)
    print(len, fc)



