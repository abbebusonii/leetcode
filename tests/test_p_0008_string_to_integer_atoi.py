import pytest
import os

pytestmark = pytest.mark.parametrize(
    "solution_fixture",
    [os.path.basename(os.path.abspath(__file__)).replace("test_", "").replace(".py", "")],
    indirect=True
)

@pytest.mark.parametrize(
    "args, expected",
    [
    # Basic Conversion
    (("42",), 42),
    (("   -42",), -42),
    (("+42",), 42),
    
    # Leading Zeros and Truncation
    (("0042",), 42),
    (("   -0042",), -42),
    
    # Non-Digit Characters
    (("4193 with words",), 4193),
    (("words and 987",), 0),
    (("123abc",), 123),
    (("123.456",), 123),
    (("3.14159",), 3),
    (("123e10",), 123),
    
    # Sign Handling
    (("--123",), 0),
    (("++123",), 0),
    (("-+12",), 0),
    ((" + 123",), 0),
    (("-a123",), 0),
    ((" +",), 0),
    ((" -",), 0),
    
    # Empty/Whitespace Inputs
    (("",), 0),
    (("   ",), 0),
    
    # Boundary Values
    (("2147483647",), 2147483647),
    (("-2147483648",), -2147483648),
    (("2147483648",), 2147483647),
    (("-2147483649",), -2147483648),
    (("999999999999999999",), 2147483647),
    (("-999999999999999999",), -2147483648),
    (("21474836460",), 2147483647),
    
    # Mixed Cases
    (("   -00123a45",), -123),
    (("123-",), 123),
    ((" -  123",), 0),
    ],
)
def test_mtAtoi(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sol.myAtoi(*args) == expected