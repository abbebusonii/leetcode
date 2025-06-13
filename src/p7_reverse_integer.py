class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rx, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rx = rx * 10 + mod
            if rx > 2**31 - 1:
                return 0
        return sign * rx