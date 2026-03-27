from typing import List
from collections import defaultdict
class Solution:
    # the time complexity of this function is O(n - k log k) where n is for the number of words and k is for the average length of a wordfor each of the n words, sorted(word) costs O(k log k)
    # while the space Complexity is O(n - k) for storing every character for every word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            output[tuple(sorted(word))].append(word)
        return list(output.values())

strs=["act","pots","tops","cat","stop","hat"]
output = Solution()
print(output.groupAnagrams(strs))
