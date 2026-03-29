from typing import List
class Solution:
    # Time complexity - O(n) : we iterate through the list once to create a set
    # Space complexity - O(n) : we create a set that can potentially store all elements
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# main test cases
if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1,2,3,1])) # -> True
    print(s.hasDuplicate([1,2,3,4])) # -> False
    print(s.hasDuplicate([1,1,1,3,3,4,3,2,4,2])) # -> True