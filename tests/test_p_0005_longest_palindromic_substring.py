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
        (("babad",), "bab"),  # "aba" is also valid, but LeetCode example uses "bab"
        (("cbbd",), "bb"),
        
        # Single character and uniform characters
        (("a",), "a"),
        (("aa",), "aa"),
        (("aaa",), "aaa"),
        (("aaaa",), "aaaa"),
        
        # Odd-length palindromes
        (("abcba",), "abcba"),  # centered single character
        (("abcdc",), "cdc"),    # centered not at middle
        
        # Even-length palindromes
        (("abba",), "abba"),    # centered between two characters
        (("abb",), "bb"),       # even-length at the start
        
        # Multiple same characters
        (("abbb",), "bbb"),
        (("abbbc",), "bbb"),
        
        # Longer palindromes in mixed strings
        (("abcddcba",), "abcddcba"),        # entire string is palindrome
        (("xabcddcbay",), "abcddcba"),      # palindrome in the middle
        (("xabcddcba",), "abcddcba"),       # palindrome at the end
        (("abcddcbax",), "abcddcba"),       # palindrome at the start
        (("abcdfdcec",), "cdfdc"),          # palindrome not at edges
    ],
)
def test_longestPalindrome(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sol.longestPalindrome(*args) in expected