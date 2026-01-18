class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read=write=0
        n=len(nums)
        while read<n:
            if nums[read]!=0:
                nums[read],nums[write]=nums[write],nums[read]
                write+=1
            read+=1
        print(nums)
