class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result=[]
        p_count=Counter(p)
        for right in range(len(s)):
            substring=s[right:right+len(p)]
            c=Counter(substring)
            if p_count==c:
                result.append(right)
        return result        