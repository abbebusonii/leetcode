import pytest
import os
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_list_node(arr: List[int]):
    list_node = ListNode()
    head = list_node
    for _, val in enumerate(arr):
        list_node.next = ListNode(val)
        list_node = list_node.next
    return head.next
    
def list_node_to_array(list_node: ListNode):
    arr = []
    while list_node:
        arr.append(list_node.val)
        list_node = list_node.next
    print(arr)
    return arr

pytestmark = pytest.mark.parametrize(
    "solution_fixture",
    [os.path.basename(os.path.abspath(__file__)).replace("test_", "").replace(".py", "")],
    indirect=True
)

@pytest.mark.parametrize(
    "args, expected",
    [
        ((array_to_list_node([2, 4, 3]), array_to_list_node([5, 6, 4]),), [7, 0, 8]),
        ((array_to_list_node([1, 0, 0, 1]), array_to_list_node([7, 8, 9, 4]),), [8, 8, 9, 5]),
        ((array_to_list_node([9, 9, 9, 9]), array_to_list_node([9, 9, 9, 9, 9, 9])), [8, 9, 9, 9, 0, 0, 1]),
        ((array_to_list_node([1, 1, 1]), array_to_list_node([1, 1, 1])), [2, 2, 2]),
        ((array_to_list_node([9, 9, 9]), array_to_list_node([1])), [0, 0, 0, 1]),
        ((array_to_list_node([7, 7, 7]), array_to_list_node([7, 7, 7])), [4, 5, 5, 1]),
        ((array_to_list_node([2]), array_to_list_node([3])), [5]),
        ((array_to_list_node([0]), array_to_list_node([0])), [0]),
        ((array_to_list_node([0]), array_to_list_node([10])), [0, 1]),
        ((array_to_list_node([0, 0, 1]), array_to_list_node([0, 0, 9])), [0, 0, 0, 1]),
    ],
)
def test_addTwoNumbers(args, expected, solution_fixture):
    sol = solution_fixture()
    assert list_node_to_array(sol.addTwoNumbers(*args)) == expected