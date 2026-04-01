from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # recursive
    # Time complexity - O(n)
    # Space complexity - O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(newHead.next)
            head.next.next = head
        head.next = None
        return newHead

# main test cases
if __name__ == "__main__":
    s = Solution()
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = s.reverseList(head)
    # print the reversed linked list
    while reversed_head:
        print(reversed_head.val) # -> 5, 4, 3, 2, 1
        reversed_head = reversed_head.next