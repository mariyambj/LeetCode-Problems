class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        if len(s) <= 1:
            return s
        for i in range(len(s)-1):
            left=i
            right=i
            while left >=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
                substring=s[left+1:right]
                if len(substring) > len(longest):
                    longest=substring
            
            left=i
            right=i+1
            while left >=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
                substring=s[left+1:right]
                if len(substring) > len(longest):
                    longest=substring
        return longest
        