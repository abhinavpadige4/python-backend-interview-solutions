# Solution for LeetCode 88: Merge Sorted Array
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge two sorted arrays into nums1.
        
        Time Complexity: O(m + n) - we traverse both arrays once
        Space Complexity: O(1) - we modify nums1 in-place
        
        Args:
            nums1: First sorted array with enough space to hold both arrays
            m: Number of valid elements in nums1
            nums2: Second sorted array
            n: Number of valid elements in nums2
            
        Returns:
            None (modifies nums1 in-place)
        """
        # Start from the end of both arrays
        p1 = m - 1  # Pointer for nums1's valid elements
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for the end of merged array
        
        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print("Test 1:", nums1)  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print("Test 2:", nums1)  # Expected: [1]
    
    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print("Test 3:", nums1)  # Expected: [1]