# Solution for LeetCode 152: Maximum Product Subarray
class Solution:
    def maxProduct(self, nums):
        """
        Given an integer array nums, find a subarray that has the largest product, and return the product.
        
        Time Complexity: O(n) - we traverse the array once
        Space Complexity: O(1) - we use constant extra space
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum product of any subarray
        """
        if not nums:
            return 0
        
        # Initialize variables to track max and min products ending at current position
        # We need to track both because a negative number can make a min product become max when multiplied by another negative
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            # If current number is negative, swapping max and min will help
            # because multiplying by negative makes big numbers small and small numbers big
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update max and min products ending at current position
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            
            # Update overall result
            result = max(result, max_product)
        
        return result

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [2,3,-2,4]
    result = solution.maxProduct(nums)
    print("Test 1:", nums, "->", result)  # Expected: 6 (from [2,3])
    
    # Test case 2
    nums = [-2,0,-1]
    result = solution.maxProduct(nums)
    print("Test 2:", nums, "->", result)  # Expected: 0
    
    # Test case 3
    nums = [-2,3,-4]
    result = solution.maxProduct(nums)
    print("Test 3:", nums, "->", result)  # Expected: 24 (from [-2,3,-4])