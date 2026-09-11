# Solution for LeetCode 21: Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists and return it as a new sorted list.
        
        Time Complexity: O(n + m) - we traverse both lists once
        Space Complexity: O(1) - we rearrange existing nodes
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            Head of the merged sorted linked list
        """
        # Create a dummy node to serve as the start of the result list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining elements
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        return dummy.next

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
    solution = Solution()
    
    # Test case 1: [1,2,4] and [1,3,4] -> [1,1,2,3,4,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print("Test 1:", linked_list_to_list(merged))  # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test case 2: [] and [] -> []
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    print("Test 2:", linked_list_to_list(merged))  # Expected: []
    
    # Test case 3: [] and [0] -> [0]
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    print("Test 3:", linked_list_to_list(merged))  # Expected: [0]