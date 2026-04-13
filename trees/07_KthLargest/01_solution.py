from typing import List
class KthLargest:

    # Time  — O(n log n) per add call: full sort on every insertion
    # Space — O(n): storing all numbers
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums)-self.k]

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
