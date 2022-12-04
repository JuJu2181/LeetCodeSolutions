"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """method 1"""
        #firstly find the total no of nodes in the linked list so that we can find the middle position of linked list
        len_list = 0 
        curr = head 
        while curr is not None:
            len_list += 1
            curr = curr.next 
        #loop to the middle node position, use floor division
        pos = 0
        while pos < len_list//2:
            head = head.next 
            pos += 1
        #return the head position which will be head of middle element
        return head
        
        """Using List"""
        # nodes_list = []
        # while head:
        #     nodes_list.append(head)
        #     head = head.next
        # #get the middle position from list
        # middle_pos = len(nodes_list)//2
        # return nodes_list[middle_pos]