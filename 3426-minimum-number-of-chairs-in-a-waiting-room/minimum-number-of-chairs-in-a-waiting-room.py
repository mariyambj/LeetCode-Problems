class Solution:
    def minimumChairs(self, s: str) -> int:
        count=max_count=0
        for i in s:
            if i=='E':
                count+=1
            if i=='L':
                count-=1
            max_count=max(count,max_count)
        return max_count

        