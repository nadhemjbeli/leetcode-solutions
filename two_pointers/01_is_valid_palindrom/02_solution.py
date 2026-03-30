class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Complexity:

        # Time  — O(n): single pass with two pointers directly on original string
        # Space — O(1): no extra string built, pointers move in place


        def alphaNum(c: str) -> bool:
            if (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')):
                return True
            return False
            
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while l < r and not alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
# main test cases
if __name__ == "__main__":
    s = Solution()
    
    # valid palindrome - ignoring non-alphanumeric and case
    print(s.isPalindrome("A man, a plan, a canal: Panama"))

    # invalid palindrome - ignoring non-alphanumeric and case
    print(s.isPalindrome("race a car"))