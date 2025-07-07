from typing import Optional

from Leetcode.permutations import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()

        left_center = left
        right_center = right

        while head:
            if head.val < x:
                left_center.next = head
                left_center = left_center.next
            else:
                right_center.next = head
                right_center = right_center.next

            head = head.next

        left_center.next = right.next
        right_center.next = None
        return left.next

    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes to start the lists for elements less than x and not less than x
        less_head = ListNode()
        not_less_head = ListNode()

        # Tail pointers for each list, which will help in appending new nodes
        less_tail = less_head
        not_less_tail = not_less_head

        # Traverse the original list
        while head:
            # If the current value is less than x, append it to the list of less_tail
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            # If the current value is not less than x, append it to the list of not_less_tail
            else:
                not_less_tail.next = head
                not_less_tail = not_less_tail.next
            # Move to the next node in the original list
            head = head.next

        # Connect the two lists together
        less_tail.next = not_less_head.next
        # The last node of the new list should point to None to indicate the end of the list
        not_less_tail.next = None

        # Return the head of the list with nodes less than x followed by nodes not less than x
        return less_head.next



def printList(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Creating the linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
    head =ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    x = 3
    h = Solution().partition(head, x)
    printList(h)

