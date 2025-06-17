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
        # Official examples
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        
        # Single row cases
        (("A", 1), "A"),
        (("AB", 1), "AB"),
        (("ABC", 1), "ABC"),
        
        # Two rows cases
        (("ABCD", 2), "ACBD"),
        (("ABCDE", 2), "ACEBD"),
        (("ABCDEF", 2), "ACEBDF"),
        
        # Three rows cases
        (("ABCD", 3), "ABDC"),
        (("ABCDEFG", 3), "AEBDFCG"),
        (("ABCDEFGHIJ", 3), "AEIBDFHJCG"),
        
        # Four rows cases
        (("ABCDEF", 4), "ABFCED"),
        (("G", 4), "G"),
        
        # Rows > string length
        (("AB", 5), "AB"),
        (("ABCD", 10), "ABCD"),
        
        # Edge cases
        (("", 3), ""),
        (("A", 100), "A"),
        
        # Complex cases
        (("HELLO.WORLD", 5), "HREOLLWDL.O"),
        (("ZIGZAGCONVERSION", 6), "ZEIVRGNSZOIACOGN"),
    ],
)
def test_convert(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sol.convert(*args) in expected