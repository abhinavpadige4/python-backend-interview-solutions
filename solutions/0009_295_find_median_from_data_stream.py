# Solution for LeetCode 295: Find Median from Data Stream
import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize data structure to find median from data stream.
        
        Time Complexity: O(log n) for addNum, O(1) for findMedian
        Space Complexity: O(n) - we store all numbers in two heaps
        
        Uses two heaps:
        - max_heap (left): stores the smaller half of numbers (as negatives for max-heap simulation)
        - min_heap (right): stores the larger half of numbers
        """
        # Max heap for the smaller half (store negatives to simulate max heap)
        self.max_heap = []  
        # Min heap for the larger half
        self.min_heap = []

    def addNum(self, num: int) -> None:
        """
        Add a number to the data stream.
        
        Args:
            num: Integer to add to the stream
        """
        # Add to max_heap first (as negative for max heap behavior)
        heapq.heappush(self.max_heap, -num)
        
        # Balance: ensure every element in max_heap <= every element in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            # Move the largest element from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Balance heap sizes: ensure size difference is at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            # Move from min_heap to max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        """
        Return the median of all elements so far.
        
        Returns:
            Median as float
        """
        if len(self.max_heap) > len(self.min_heap):
            # Odd number of elements, max_heap has one more
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            # Odd number of elements, min_heap has one more
            return self.min_heap[0]
        else:
            # Even number of elements, average of both tops
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

# Test the solution
if __name__ == "__main__":
    # Test case from LeetCode example
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # returns 1.5
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # returns 2.0
    
    # Additional test cases
    print("\nAdditional tests:")
    medianFinder2 = MedianFinder()
    medianFinder2.addNum(5)
    print("After adding 5:", medianFinder2.findMedian())  # 5.0
    medianFinder2.addNum(3)
    print("After adding 3:", medianFinder2.findMedian())  # 4.0
    medianFinder2.addNum(4)
    print("After adding 4:", medianFinder2.findMedian())  # 4.0
    medianFinder2.addNum(2)
    print("After adding 2:", medianFinder2.findMedian())  # 3.5
    medianFinder2.addNum(6)
    print("After adding 6:", medianFinder2.findMedian())  # 4.0