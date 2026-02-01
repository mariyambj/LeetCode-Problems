class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        p_count=Counter(s1)
        for right in range(len(s2)-len(s1)+1):
            substring=s2[right:right+len(s1)]
            c=Counter(substring)
            if p_count==c:
                return True
        return False 