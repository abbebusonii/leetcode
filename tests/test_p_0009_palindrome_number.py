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
        ((123,), False),
        ((1234,), False),
        ((121,), True),
        ((1221,), True),
        ((-15512,), False),
        ((0,), True),
        ((100,), False),
        ((10,), False),
        ((4,), True),
        ((-5,), False),
        ((7100842007,), False),
        ((678429924876,), True),
        ((6784296924876,), True),
        ((10000001,), True),
    ],
)
def test_isPalindrome(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sol.isPalindrome(*args) == expected