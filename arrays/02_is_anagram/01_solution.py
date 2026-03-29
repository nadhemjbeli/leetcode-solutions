
## this has time complexity O(n) and 
## space complexity O(n) because of the two dictionaries
from collections import Counter
def isAnagram(s: str, t: str) -> bool:
   return Counter(s) == Counter(t)


print("isAnagram('cat', 'act') : ", isAnagram("cat","act")) # -> True
print("isAnagram('four', 'roof') : ", isAnagram("four", "roof")) # -> False
print("isAnagram('foore', 'roof') : ", isAnagram("foore", "roof")) # -> False
