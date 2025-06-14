class Solution:
    def myAtoi(self, s: str) -> int:
        ans = []
        digits = set(str(i) for i in range(10))
        s = s.lstrip(" ")
        if not s:
            return 0
        sign = -1 if s[0] == "-" else 1
        if s[0] in ("-", "+"):
            s = s[1:]
        if not s:
            return 0
        s = s.lstrip("0")
        if not s:
            return 0
        for c in s:
            if c not in digits:
                break
            ans.append(c)
        if not ans:
            return 0
        ans = int("".join(c for c in ans))
        return min(ans, 2 ** 31 - 1) if sign == 1 else max(sign * ans, -2 ** 31)