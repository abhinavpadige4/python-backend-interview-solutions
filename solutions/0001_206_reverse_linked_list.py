# Solution for LeetCode 206: Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverse a singly linked list.
        
        Time Complexity: O(n) - we visit each node once
        Space Complexity: O(1) - we use constant extra space
        
        Args:
            head: Head of the linked list
            
        Returns:
            New head of the reversed linked list
        """
        prev = None
        current = head
        
        while current:
            # Store next node
            next_temp = current.next
            # Reverse current node's pointer
            current.next = prev
            # Move pointers forward
            prev = current
            current = next_temp
            
        return prev

# Helper function to create linked list from list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    reversed_head = solution.reverseList(head)
    print("Original:", [1, 2, 3, 4, 5])
    print("Reversed:", linked_list_to_list(reversed_head))
    
    # Test case 2: [1,2] -> [2,1]
    head2 = create_linked_list([1, 2])
    reversed_head2 = solution.reverseList(head2)
    print("Original:", [1, 2])
    print("Reversed:", linked_list_to_list(reversed_head2))
    
    # Test case 3: [] -> []
    head3 = create_linked_list([])
    reversed_head3 = solution.reverseList(head3)
    print("Original:", [])
    print("Reversed:", linked_list_to_list(reversed_head3))