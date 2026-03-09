class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        close=nums[0]+nums[1]+nums[2]
        sum_=0
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left< right:
                sum_=nums[left] + nums[i] + nums[right] 
                if abs(target-sum_)< abs(target-close):
                    close=sum_
                if sum_ <target:
                    left+=1
                else:
                    right-=1
        return close



        
        