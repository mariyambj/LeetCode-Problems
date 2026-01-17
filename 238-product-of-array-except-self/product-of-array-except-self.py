class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''n=len(nums)
        prefix=[1]*n
        prefix_=1
        for i in range(n):
            prefix[i]=prefix_
            prefix_*=nums[i]
        suffix=[1]*n
        suffix_=1
        for i in range(n-1,-1,-1):
            suffix[i]=suffix_
            suffix_*=nums[i]
        while n>0:
            n-=1
            prefix[n]=prefix[n]*suffix[n]
        return prefix'''
        n=len(nums)
        output=[1]*n
        prefix=1
        for i in range(n):
            output[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            output[i]*=suffix
            suffix*=nums[i]
        return output


        