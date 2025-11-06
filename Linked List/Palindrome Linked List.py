class Solution:
    def isPalindrome(self, head):
        # Step 1: Find the middle using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare both halves
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True
