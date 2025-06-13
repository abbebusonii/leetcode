class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        bound = "2147483647" if sign == 1 else "2147483648"
        x = str(x)[::-1] if sign == 1 else str(x)[1:][::-1]
        n = len(x)
        if n < len(bound):
            return sign * int(x)
        i = 0
        while i < n:
            if x[i] > bound[i]:
                return 0
            elif x[i] < bound[i]:
                break
            i += 1
        return sign * int(x)