import pytest
from src.p7_reverse_integer import Solution

@pytest.mark.parametrize(
    "input_val, expected",
    [
        # Basic positive and negative numbers
        (123, 321),
        (-123, -321),
        # Trailing zeros become leading zeros (dropped during conversion)
        (120, 21),
        (100, 1),
        # Zero handling
        (0, 0),
        # Numbers causing overflow when reversed
        (1534236469, 0),
        (-1534236469, 0),
        (2147483647, 0),  # Max 32-bit int reversed overflows
        (-2147483648, 0), # Min 32-bit int reversed overflows
        # Valid reversals within bounds
        (2147483641, 1463847412),
        (-2147483641, -1463847412),
        (123456789, 987654321),
        # Multi-digit with internal zeros
        (1000000002, 2000000001),  # Reversed within bounds
        (1234567890, 987654321),   # Leading zero in reversal
        # Numbers where reversed digits match bound length
        (1234567899, 0),        # First digit exceeds bound
        (1000000003, 0),        # First digit exceeds bound (3>2)
        (-1000000003, 0),       # Absolute reversal exceeds negative bound
        # Negative reversals within bounds
        (-1000000002, -2000000001),
        # Larger magnitude but still within bounds
        (1463847412, 2147483641),
        (-1463847412, -2147483641),
    ],
)
def test_reverse(input_val, expected):
    sol = Solution()
    assert sol.reverse(input_val) == expected