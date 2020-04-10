# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert(self, head, data): 
        while head.next: 
            head = head.next 
        head.next = ListNode(data)

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        return slow


head = [1,2,3,4,5]
solution = Solution()
node = ListNode(head[0])
for i in head[1:]: 
    node.insert(node, i)

node = solution.middleNode(node)
print(node.val)