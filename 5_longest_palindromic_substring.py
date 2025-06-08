class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def check(i, j):
            l = 0
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                l = j - i + 1
                i -= 1
                j += 1
            return l
        ans = [0, 0]
        for i in range(1, n):
            l_odd = check(i, i)
            l_even = check(i - 1, i)
            if l_odd > ans[1] - ans[0] + 1:
                half = (l_odd - 1) // 2
                ans = [i - half, i + half]
            if l_even > ans[1] - ans[0] + 1:
                half = l_even // 2
                ans = [i - half, i + half - 1]
        return s[ans[0]:ans[1] + 1]