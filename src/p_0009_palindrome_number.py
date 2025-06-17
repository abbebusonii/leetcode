class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rx = 0
        copy = x
        while copy:
            copy, reminder = divmod(copy, 10)
            rx = 10 * rx + reminder
        return rx == x