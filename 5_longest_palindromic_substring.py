class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        matrix = [[False for _ in range(n)] for _ in range(n)]
        ans = [0, 0]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 1:
                    matrix[i][j] = True
                elif l == 2:
                    matrix[i][j] = s[i] == s[j]
                else:
                    matrix[i][j] = s[i] == s[j] and matrix[i + 1][j - 1]
                if matrix[i][j] and l > ans[1] - ans[0] + 1:
                    ans = [i, j]
        return s[ans[0]:ans[1] + 1]