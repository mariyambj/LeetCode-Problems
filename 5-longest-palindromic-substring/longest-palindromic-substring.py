class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str=s[0]
        max_len=0
        if len(s) <= 1:
            return s
        for left in range(len(s)):
            for right in range(left+1,len(s)):
                substring=s[left:right+1]
                if right - left + 1 > max_len and substring == substring[::-1]:
                    max_len= right - left + 1
                    max_str=substring
        return max_str
        