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
        # Example from problem: total odd length
        (([1, 3], [2]), 2.0),
        # Example from problem: total even length
        (([1, 2], [3, 4]), 2.5),
        # Both arrays non-empty, total even (zeros)
        (([0, 0], [0, 0]), 0.0),
        # Second array empty, first has odd length
        (([1, 2, 3], []), 2.0),
        # First array empty, second has even length
        (([], [1, 2, 3, 4]), 2.5),
        # Both non-empty, total odd (7 elements)
        (([1, 3, 5, 7], [2, 4, 6]), 4.0),
        # Negative numbers, total odd (5 elements)
        (([-5, -3, -1], [-2, 0]), -2.0),
        # Duplicates, total even (8 elements)
        (([1, 1, 3, 3], [1, 1, 3, 3]), 2.0),
        # First array has 1 element, second has 3 (total even)
        (([1], [2, 3, 4]), 2.5),
        # Identical arrays
        (([5, 5], [5, 5]), 5),
    ],
)
def test_findMedianSortedArrays(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sol.findMedianSortedArrays(*args) == expected