class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        n = len(s)
        for l in range(n, 0, -1):
            for start in range(n - l + 1):
                if check(start, start + l - 1):
                    return s[start:start + l]