# Solution for LeetCode 560: Subarray Sum Equals K
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
        
        Time Complexity: O(n) - we traverse the array once
        Space Complexity: O(n) - we store prefix sums in a hash map
        
        Args:
            nums: List of integers
            k: Target sum
            
        Returns:
            Number of subarrays that sum to k
        """
        # Dictionary to store frequency of prefix sums
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: empty subarray has sum 0
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            # If (current_sum - k) exists in prefix_sum_count, 
            # it means there's a subarray ending at current index with sum k
            if (current_sum - k) in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            
            # Increment the count of current prefix sum
            prefix_sum_count[current_sum] += 1
        
        return count

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [1,1,1]
    k = 2
    result = solution.subarraySum(nums, k)
    print("Test 1:", nums, "k=", k, "->", result)  # Expected: 2 ([1,1] and [1,1])
    
    # Test case 2
    nums = [1,2,3]
    k = 3
    result = solution.subarraySum(nums, k)
    print("Test 2:", nums, "k=", k, "->", result)  # Expected: 2 ([1,2] and [3])
    
    # Test case 3
    nums = [1]
    k = 0
    result = solution.subarraySum(nums, k)
    print("Test 3:", nums, "k=", k, "->", result)  # Expected: 0
    
    # Test case 4
    nums = [1,-1,0]
    k = 0
    result = solution.subarraySum(nums, k)
    print("Test 4:", nums, "k=", k, "->", result)  # Expected: 3 ([1,-1], [0], [1,-1,0])