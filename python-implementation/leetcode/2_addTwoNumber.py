'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x=0, next=None, node_list=None):
        self.val = x
        self.next = next
        if node_list is not None:
            self.set_value(node_list)

    def __str__(self):
        current_node = self
        print_v = ''
        while current_node is not None:
            print_v += str(current_node.val) + ','
            current_node = current_node.next
        return print_v

    def set_value(self, list_v):
        current_node = self
        current_node.val = list_v[0]
        count = 1
        while count < len(list_v):
            current_node.next = ListNode(list_v[count])
            current_node = current_node.next
            count += 1

    def get_node_len(self):
        length = 0
        current_node = self
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length


def addNumber(list_node, number):
    new_val = list_node.val + number
    if new_val > 9:
        list_node.val = new_val - 10
        if list_node.next is not None:
            addNumber(list_node.next, 1)
        else:
            list_node.next = ListNode(1)
    else:
        list_node.val = new_val
    return list_node


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1_len = l1.get_node_len()
    l2_len = l2.get_node_len()

    base_node = l1 if l1_len > l2_len else l2
    add_node = l2 if l1_len > l2_len else l1

    while add_node is not None:
        addNumber(base_node, add_node.val)
        base_node = base_node.next
        add_node = add_node.next

    return l1 if l1_len > l2_len else l2


def addTwoNumbers1(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    elif l2 == None:
        return l1

    remain = 0
    l = ListNode(None)
    result = l

    while l1 != None or l2 != None:
        if l1 == None:
            l1 = ListNode(0)
        elif l2 == None:
            l2 = ListNode(0)
        total = l1.val + l2.val + remain
        if total >= 10:
            total = total - 10
            remain = 1
        else:
            remain = 0
        l.next = ListNode(total)
        l1 = l1.next
        l2 = l2.next
        l = l.next

    if remain == 1:
        l.next = ListNode(remain)

    return result.next


import unittest


class TestCases(unittest.TestCase):

    def listNodeEqual(self, node1, node2, msg='Node List are not equal'):
        if str(node1) == str(node2):
            return
        msg = str(node1) + " is not equal to " + str(node2)
        raise self.failureException(msg)

    def setUp(self):
        self.addTypeEqualityFunc(ListNode, self.listNodeEqual)

    def testCase1(self):
        l1_node = ListNode(node_list=[2, 4, 3])
        l2_node = ListNode(node_list=[5, 6, 4])
        expectation = ListNode(node_list=[7, 0, 8])
        self.assertEqual(addTwoNumbers(l1_node, l2_node), expectation)

    def testCase2(self):
        l1_node = ListNode(node_list=[1])
        l2_node = ListNode(node_list=[9, 9, 9])
        expectation = ListNode(node_list=[0, 0, 0, 1])
        self.assertEqual(addTwoNumbers(l1_node, l2_node), expectation)
