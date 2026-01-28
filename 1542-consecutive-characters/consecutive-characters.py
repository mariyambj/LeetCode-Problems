class Solution:
    def maxPower(self, s: str) -> int:
        count=max_count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1
            max_count=max(count,max_count)
        return max_count


        