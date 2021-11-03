# Given the head of a linked list,
# remove the nth node from the end of the list
# and return its head.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.head = None
        self.n = None

    def removenthNode(self):
        size = 1
        cur = p = self.head

        while cur.next:
            size += 1
            cur.next = ListNode()
            if size > n+1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head


result = Solution()
result.removenthNode()

result.removenthNode([1,2,3,4,5,6], n=2)




print(result)