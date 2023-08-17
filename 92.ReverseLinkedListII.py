# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        prev=curr
        after=curr
        vals=[]
        i=1

        if (i == left):
            iIn=i
            while(i<=right and after):  
                vals.append(after.val)
                i+=1
                after=after.next
            print(vals)
            for i in range(iIn , i):
                prev.val=vals.pop()
                prev=prev.next
            return head

        while(i+1<left):
            prev=prev.next
            i+=1
        after=prev            
        iIn=i
        while(i<right and after.next):
            after=after.next
            i+=1
            vals.append(after.val)
        prev=prev.next
        print(vals)
        for i in range(iIn , i):
            prev.val=vals.pop()
            prev=prev.next

        return head
