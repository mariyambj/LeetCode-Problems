class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        balance={}
        for i in range(len(nums)):
            bal=target-nums[i]
            if nums[i] in balance:
                return [balance[nums[i]],i]
            balance[bal]=i
    
            '''        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return (i,j)
        '''