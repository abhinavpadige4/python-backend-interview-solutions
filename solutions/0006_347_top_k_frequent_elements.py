# Solution for LeetCode 347: Top K Frequent Elements
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        
        Time Complexity: O(n log k) - we process n elements and heap operations are O(log k)
        Space Complexity: O(n) - we store frequency count for all elements
        
        Args:
            nums: List of integers
            k: Number of top frequent elements to return
            
        Returns:
            List of k most frequent elements
        """
        # Count frequency of each element
        freq_map = Counter(nums)
        
        # Use a min-heap to keep track of top k elements
        # We store (frequency, element) and keep smallest frequencies at top
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            # Keep heap size at most k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract elements from heap
        result = []
        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)
        
        return result

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [1,1,1,2,2,3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print("Test 1:", nums, "k=", k, "->", sorted(result))  # Expected: [1, 2]
    
    # Test case 2
    nums = [1]
    k = 1
    result = solution.topKFrequent(nums, k)
    print("Test 2:", nums, "k=", k, "->", result)  # Expected: [1]
    
    # Test case 3
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print("Test 3:", nums, "k=", k, "->", sorted(result))  # Expected: [-1, 2]