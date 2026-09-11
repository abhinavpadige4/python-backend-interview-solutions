# Solution for LeetCode 238: Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums):
        """
        Given an integer array nums, return an array answer such that 
        answer[i] is equal to the product of all the elements of nums except nums[i].
        
        Time Complexity: O(n) - we make two passes through the array
        Space Complexity: O(1) excluding the output array - we use constant extra space
        
        Args:
            nums: List of integers
            
        Returns:
            List of products where each element is product of all other elements
        """
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products (products of all elements to the left)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [1, 2, 3, 4]
    result = solution.productExceptSelf(nums)
    print("Test 1:", nums, "->", result)  # Expected: [24, 12, 8, 6]
    
    # Test case 2
    nums = [-1, 1, 0, -3, 3]
    result = solution.productExceptSelf(nums)
    print("Test 2:", nums, "->", result)  # Expected: [0, 0, 9, 0, 0]
    
    # Test case 3
    nums = [5]
    result = solution.productExceptSelf(nums)
    print("Test 3:", nums, "->", result)  # Expected: [1]