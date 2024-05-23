# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
    
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        def len_head(head):
            count = 0
            while head:
                count = count+1
                head = head.next
            return count 

        count = len_head(head)

        if count == n :
            head = head.next
            return head

        copy = head
        n = count - n - 1
        count = 0
        print(n)
        if n >= 0:
            print("in if")
            while copy:
                if count == n:
                    copy.next = copy.next.next
                count += 1
                copy = copy.next
            
            return head

         








        