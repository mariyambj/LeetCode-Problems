class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count=0
        max_count=cur_one=0
        for end in range(len(nums)):
            if nums[end]==1:
                one_count+=1
                cur_one=one_count
            if nums[end]==0:
                one_count=0
            max_count=max(cur_one,max_count)
        return max_count


        