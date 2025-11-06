class Solution:
    def intersectPoint(self, head1, head2):
        # Step 1: Get lengths of both lists
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        len1 = getLength(head1)
        len2 = getLength(head2)

        # Step 2: Advance the longer list by the difference in lengths
        diff = abs(len1 - len2)
        if len1 > len2:
            for _ in range(diff):
                head1 = head1.next
        else:
            for _ in range(diff):
                head2 = head2.next

        # Step 3: Traverse both lists together to find intersection
        while head1 and head2:
            if head1 == head2:
                return head1.data
            head1 = head1.next
            head2 = head2.next

        return -1  # No intersection
