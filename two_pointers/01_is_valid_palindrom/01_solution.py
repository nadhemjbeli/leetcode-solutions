class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Complexity:

        # Time  — O(n): one pass to filter, one pass with two pointers — both linear, n is len(s)
        # Space — O(n): res string holds up to n characters in the worst case (all alphanumeric)

        res=''

        def alphaNum(c: str) -> bool:
            if (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')):
                return True
            return False
            
        for c in s:
            if alphaNum(c):
                res+=c
        
        l, r = 0, len(res) - 1
        while l<r:
            if res[l].lower()!=res[r].lower():
                return False
            l+=1
            r-=1
        return True
    
# main test cases
if __name__ == "__main__":
    s = Solution()
    
    # valid palindrome - ignoring non-alphanumeric and case
    print(s.isPalindrome("A man, a plan, a canal: Panama"))

    # invalid palindrome - ignoring non-alphanumeric and case
    print(s.isPalindrome("race a car"))