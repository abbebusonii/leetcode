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
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkeww1123456789",), 9),
    (("abcdefg",), 7),
    (("",), 0),
    (("aaaaaaaambnmnmnaaaa",), 4),
    (("bbbbbcdfghjkaaaaaa",), 9),
    (("44a881555",), 3),
    (("000",), 1),
    (("188488",), 2),
    (("m",), 1),
    ],
)
def test_lengthOfLongestSubstring(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sol.lengthOfLongestSubstring(*args) == expected