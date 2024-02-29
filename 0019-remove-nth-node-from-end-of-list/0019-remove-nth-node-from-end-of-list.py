class Solution:
    def removeNthFromEnd(self, head, n):
        if head:
            # Create a dummy node to handle edge cases
            dummy = ListNode(0)
            dummy.next = head
            fast = dummy
            slow = dummy
            # Move fast pointer n+1 steps ahead
            for _ in range(n + 1):
                fast = fast.next
            # Move fast to the end, maintaining the gap of n nodes
            while fast:
                fast = fast.next
                slow = slow.next
            # Remove the Nth node from the end
            slow.next = slow.next.next
            # Return the head of the modified list
            return dummy.next