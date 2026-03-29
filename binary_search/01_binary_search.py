from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity - O(log n) : we halve the search space on every iteration
        # Space complexity - O(1) : only three pointers, no extra data structure
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
# main test cases
if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9)) # -> 4
    print(s.search([-1,0,3,5,9,12], 2)) # -> -1 