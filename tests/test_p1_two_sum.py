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
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([-1, -2, -3, -4, -5], -8), [2, 4]),
        (([-3, 4, 3, 90], 0), [0, 2]),
        (([10, 1, 2, 3, 4, 5], 15), [0, 5]),
        (([1, 2], 3), [0, 1]),
        (([1, 2, 3, 4, 8], 7), [2, 3]),
        (([0, 0], 0), [0, 1]),
        (([0, 1, 0, 2], 3), [1, 3]),
        (([1, 5, 3, 7], 10), [2, 3]),
        (([-5, 1, 2, 3, 4], -1), [0, 4]),
    ],
)
def test_twoSum(args, expected, solution_fixture):
    sol = solution_fixture()
    assert sorted(sol.twoSum(*args)) == expected