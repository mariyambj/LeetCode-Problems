class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag=False
        count={}
        for i in range(len(nums)):
            if nums[i] in count and abs(i-count[nums[i]]) <= k:
                flag=True
            count[nums[i]]=i
        return flag
