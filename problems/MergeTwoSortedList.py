# https://leetcode.com/problems/merge-two-sorted-lists

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    # Attach the remaining part
    current.next = l1 if l1 else l2

    return dummy.next
