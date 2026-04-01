from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity - O(n): we're iterating through the head ListNode
    # Space complexity - O(1): only 3 pointers are storing values, 
    # no need for data structures
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

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