class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last=-1,-1
        for i in range(len(nums)):
            if target==nums[i]:
                if first==-1:
                    first=i
                last=i
        return [first,last]


        