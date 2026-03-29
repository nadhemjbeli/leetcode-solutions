from typing import List
class Solution:
    # Time complexity - O(n) : we iterate through the list once to create a set
    # Space complexity - O(n) : we create a set that can potentially store numbers until it finds a duplication, worst case scenario, n is achieved
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set()

        for num in nums:
            if num in setNums:
                return True
            setNums.add(num)
        return False
# main test cases
if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1,2,3,1])) # -> True
    print(s.hasDuplicate([1,2,3,4])) # -> False
    print(s.hasDuplicate([1,1,1,3,3,4,3,2,4,2])) # -> True