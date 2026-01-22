class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return sum(nums)
        else:
            max_sum=sum(nums[:k])
            cur_sum=max_sum
            for i in range(k,len(nums)):
                cur_sum+=nums[i]
                cur_sum-=nums[i-k]
                max_sum=max(cur_sum,max_sum)
        return max_sum/k


