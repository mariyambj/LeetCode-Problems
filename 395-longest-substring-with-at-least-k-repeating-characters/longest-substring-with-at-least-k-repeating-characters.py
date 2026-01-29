class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count={}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]]=1
            else:
                count[s[i]]+=1
        for i,char in enumerate(s):
            if count[char]<k:
                left=self.longestSubstring(s[:i],k)
                right=self.longestSubstring(s[i+1:],k)
                return max(left, right)
        return len(s)
        