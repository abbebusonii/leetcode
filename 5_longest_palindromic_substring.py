class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_hash = "#" + "#".join(c for c in s) + "#"
        n = len(s_hash)
        lp = [0 if i % 2 == 0 else 1 for i in range(n)]
        center = bound = ans = 0
        for i in range(n):
            if i > bound:
                center = bound = i
            else:
                lp[i] = min(lp[2 * center - i], bound - i)
            r = lp[i]
            while i - r - 1 >= 0 and i + r + 1 < n and s_hash[i - r - 1] == s_hash[i + r + 1]:
                r += 1
                lp[i] += 2 * (s_hash[i + r] != "#")
            if i + r > bound:
                center = i
                bound = i + r
            if lp[i] > lp[ans]:
                ans = i
        return s[(ans - lp[ans]) // 2:(ans + lp[ans]) // 2]