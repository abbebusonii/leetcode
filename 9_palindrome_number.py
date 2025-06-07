class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        revx = 0
        d = x
        while d != 0:
            revx = revx * 10 + d % 10
            d //= 10
        return revx == x