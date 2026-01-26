class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum_=0
        cur_len=0
        min_len=float('inf')
        while right<len(nums):
            sum_+=nums[right]
            right+=1
            while sum_>=target:
                cur_len=right-left
                min_len=min(cur_len,min_len)
                sum_-=nums[left]
                left+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
        
            



