class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_strings=[]
        left=0
        substring=set()
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left+=1
            substring.add(s[right])
            sub_strings.append(s[left:right+1])
        return max((len(x) for x in sub_strings),default=0)



        