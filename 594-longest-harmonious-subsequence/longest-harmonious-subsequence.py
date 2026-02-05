class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        j=0
        max_len=0
        for i in range(len(nums)):
            while (nums[i]-nums[j])>1:
                j+=1
            if nums[i]-nums[j]==1:
                max_len=max(max_len,i-j+1)
        return max_len
