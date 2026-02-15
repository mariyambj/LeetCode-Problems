class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        freq=defaultdict(int)
        freq[0]=1
        prefix_sum=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-goal in freq:
                count+=freq[prefix_sum-goal]
            freq[prefix_sum]+=1
        return count
