class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count=0
        current=0
        for right in range(1,len(nums)-1):
            if nums[right] - nums[right-1]== nums[right+1] - nums[right]:
                current+=1
                count+=current
            else:
                current=0
        return count


        