from typing import List
import heapq
class KthLargest:
    # Time  — O(n log k) init, O(log k) per add call
    # Space — O(k): heap never grows beyond k elements
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# main test cases
if __name__ == "__main__":
    k = 3
    nums = [4,5,8,2]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(3))   # return 4
    print(kthLargest.add(5))   # return 5
    print(kthLargest.add(10))  # return 5
    print(kthLargest.add(9))   # return 8
    print(kthLargest.add(4))   # return 8