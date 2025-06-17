class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        while i < n and s[i] == " ":
            i += 1
        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):
            sign = -1 if s[i] == "-" else 1
            i += 1
        ans = 0
        lower_bound, upper_bound = -2 ** 31, 2 ** 31 - 1
        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            if ans * sign > upper_bound:
                return upper_bound
            if ans * sign < lower_bound:
                return lower_bound
            i += 1
        return ans * sign