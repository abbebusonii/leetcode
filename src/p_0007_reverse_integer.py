class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        bound = 2 ** 31 - 1
        rx, x = 0, abs(x)
        while x:
            x, reminder = divmod(x, 10)
            rx = rx * 10 + reminder
            if rx > bound:
                return 0
        return sign * rx