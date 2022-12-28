"""
Floyd's Tortoise and Hare algorithm is an important algorithm that can be used to detect if a linked list contains cycle or not in constant time complexity.
Unlike using a set or hashset which can detect cycle too but consumes O(n) space complexity, this algorithm can detect cycle in space complexity O(n)

- For this it makes use of 2 pointers slow and fast. 
- Slow moves one node at a time and fast moves two nodes at a time. 
- If thest two pointers don't meet at all then there is no cycle but if at any time slow == fast cycle exists
"""
class Node:
    def __init__(self,val=None,nxt=None) -> None:
        self.val = val 
        self.next = nxt 

class LinkedList:
    def __init__(self,head=None):
        self.head = head 
    
    #method to traverse and display the linked list
    def display(self):
        current = self.head 
        list_to_display = []
        while current:
            list_to_display.append(str(current.val))
            current = current.next
        print("Given Linked List is: ")
        print(" -> ".join(list_to_display))


def detect_cycle_using_floyds_algorithm(linked_list):
    # If linked list is empty no cycle is found
    if linked_list.head is None: 
        return False, None 
    #define two pointers slow and fast
    slow = linked_list.head 
    fast = slow.next 
    #Loop to see if slow ever catches fast
    while slow != fast:
        #if the next element or next next element of fast is none it means end of list so no cycle was found
        if fast.next is None or fast.next.next is None: 
            return False, None 
        #increment slow by one
        slow = slow.next 
        #increment fast by two
        fast = fast.next.next 
    #if slow catches fast cycle is detected so return True along with position where cycle was detected
    return True, slow.next


if __name__ == "__main__":
    # Initializing Linked List
    linked_list = LinkedList() 
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n1.next = n2 
    n2.next = n3
    n3.next = n4 
    n4.next = n2
    linked_list.head = n1
    #Detect cycles using Floyd's tortoise hare algorithm
    res, pos = detect_cycle_using_floyds_algorithm(linked_list)
    # if result is true cycle was found
    if res:
        print(f"Cycle was found at {pos.val}")
    else:
        # No cycles were found so display the linked list
        print("No cycles were detected")
        linked_list.display()