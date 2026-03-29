# this is of time complexity O(n) and space complexity O(1)

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dict_s, dict_t = {}, {}

    for c in s:
        dict_s[c] = dict_s.get(c, 0) + 1
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1
    return dict_s == dict_t


print("isAnagram('cat', 'act') : ", isAnagram("cat","act")) # -> True
print("isAnagram('four', 'roof') : ", isAnagram("four", "roof")) # -> False
print("isAnagram('foore', 'roof') : ", isAnagram("foore", "roof")) # -> False
